# 方圆小站Github仓库

---start---
## 目录
[建立个人独立博客有什么好处?](https://fangyuanxiaozhan.com/p/2020-01-18-blog/)

[Xbox 2020 series手柄体验实录（附自制Xbox体感射击技巧）](https://fangyuanxiaozhan.com/p/2020-01-19-xbox-2020-series/)

[zhaoolee的Github主页](https://fangyuanxiaozhan.com/p/2020-01-17-zhaoolee/)

---end---


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


