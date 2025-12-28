#!/usr/bin/env python3
# qiniu身份认证可以从qiniu.json 读取
# 格式为
# {
#     "AK":"****-J3M5OZp",
#     "SK":"****-ob"
# }

# 支持终端输入md文件的的位置（比如_posts 里面的.md文件），读取 某个.md 文件的内容，获取里面的本地图片信息，将图片上传到七牛云，并将图片链接替换为七牛云的链接，最后打印出修改后的内容，不要改写文件

QINIU_BUCKET = "tmp-blog"
QINIU_DOMAIN = "http://tmp-blog.fangyuanxiaozhan.com"
QINIU_PREFIX = "blog"

import argparse
import json
import os
import re
import sys
import urllib.parse
from qiniu import Auth, put_file

MD_IMAGE_PATTERN = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def load_auth(auth_file):
    with open(auth_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    ak = data.get("AK")
    sk = data.get("SK")
    if not ak or not sk:
        raise ValueError("Missing AK/SK in auth file.")
    return ak, sk


def parse_markdown_url(inner):
    if not inner:
        return None, None, None
    stripped = inner.lstrip()
    offset = len(inner) - len(stripped)
    if stripped.startswith("<"):
        end = stripped.find(">")
        if end != -1:
            url = stripped[1:end].strip()
            url_start = offset + 1
            url_end = offset + end
            return url, url_start, url_end
    match = re.search(r"\s", stripped)
    if match:
        url = stripped[: match.start()]
        url_start = offset
        url_end = offset + match.start()
    else:
        url = stripped
        url_start = offset
        url_end = offset + len(stripped)
    return url, url_start, url_end


def resolve_local_path(md_path, url):
    url = urllib.parse.unquote(url)
    url = url.split("#", 1)[0].split("?", 1)[0]
    if not url:
        return None
    if os.path.isabs(url):
        return url if os.path.isfile(url) else None
    candidate = os.path.normpath(os.path.join(os.path.dirname(md_path), url))
    return candidate if os.path.isfile(candidate) else None


class QiniuUploader:
    def __init__(self, auth, bucket, domain, prefix):
        self.auth = auth
        self.bucket = bucket
        self.domain = domain.strip().rstrip("/") if domain else domain
        self.prefix = prefix
        self.cache = {}

    def is_same_domain(self, url):
        if not self.domain:
            return False
        return url.startswith(self.domain + "/") or url == self.domain

    def upload_local(self, local_path):
        local_path = os.path.abspath(local_path)
        if local_path in self.cache:
            return self.cache[local_path]
        name = os.path.basename(local_path)
        key = f"{self.prefix.strip('/')}/{name}" if self.prefix else name
        new_url = self._put_file(local_path, key)
        self.cache[local_path] = new_url
        return new_url

    def _put_file(self, file_path, key):
        token = self.auth.upload_token(self.bucket, key)
        ret, info = put_file(token, key, file_path)
        status = getattr(info, "status_code", None)
        if status != 200:
            error = getattr(info, "error", "unknown error")
            raise RuntimeError(f"Upload failed for {file_path}: {error}")
        quoted = urllib.parse.quote(key, safe="/")
        return f"{self.domain}/{quoted}"


def replace_markdown_images(content, md_path, uploader):
    def replace_markdown(match):
        inner = match.group(1)
        url, start, end = parse_markdown_url(inner)
        if not url:
            return match.group(0)
        new_url = upload_image(url, md_path, uploader)
        if not new_url:
            return match.group(0)
        new_inner = inner[:start] + new_url + inner[end:]
        return match.group(0).replace(inner, new_inner, 1)

    new_content = MD_IMAGE_PATTERN.sub(replace_markdown, content)
    return new_content


def upload_image(url, md_path, uploader):
    if not url:
        return None
    url = url.strip()
    if uploader.is_same_domain(url):
        return url
    if url.startswith(("http://", "https://", "//")):
        print(f"Skip remote URL: {url}", file=sys.stderr)
        return None
    local_path = resolve_local_path(md_path, url)
    if not local_path:
        print(f"Local file not found: {url}", file=sys.stderr)
        return None
    try:
        print(f"Upload local: {local_path}", file=sys.stderr)
        return uploader.upload_local(local_path)
    except Exception as exc:
        print(f"Failed upload: {local_path} ({exc})", file=sys.stderr)
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Upload images in a Markdown file to Qiniu and print updated content."
    )
    parser.add_argument("path", nargs="?", help="Markdown file path (absolute)")
    parser.add_argument("--auth-file", default="qiniu.json", help="Qiniu auth JSON file")
    args = parser.parse_args()

    md_path = args.path
    if not md_path:
        md_path = input("请输入Markdown绝对路径: ").strip()
    if not os.path.isabs(md_path):
        print("Markdown path must be absolute.", file=sys.stderr)
        raise SystemExit(1)
    if not os.path.isfile(md_path):
        print(f"Markdown file not found: {md_path}", file=sys.stderr)
        raise SystemExit(1)
    if not QINIU_BUCKET or not QINIU_DOMAIN:
        print("Missing QINIU_BUCKET or QINIU_DOMAIN.", file=sys.stderr)
        raise SystemExit(1)

    try:
        ak, sk = load_auth(args.auth_file)
    except Exception as exc:
        print(f"Failed to read auth file: {exc}", file=sys.stderr)
        raise SystemExit(1)

    auth = Auth(ak, sk)
    uploader = QiniuUploader(auth, QINIU_BUCKET, QINIU_DOMAIN, QINIU_PREFIX)

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = replace_markdown_images(content, md_path, uploader)
    sys.stdout.write(new_content)


if __name__ == "__main__":
    main()
