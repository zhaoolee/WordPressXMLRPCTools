# 将本地Markdown同步到WordPress

- 在根目录下config.txt配置信息

用户名 username
密码   password
xmlrpc地址  xmlrpc_php



- 在`_posts` 目录下新建 `.md` 后缀的文件

- 在`.md`中填写以下初始化信息

```
---
title: Hello222
tags: 
- CallBack
- Promise
- Node.js
categories:
- 前端
---

```

- 填入正文内容后，python main.py 即可将书写的文件同步到wordpress网站


