---
title: 群晖的妙用
tags:
- 个人成长
categories:
- 杂谈
---



最近维护朋友公司内网的服务器，公司的内网安装了**绿盟的防火墙，服务器请求一些海外镜像的依赖包，IP就会被拉黑，只能内网访问**，我发现可以**先登陆群晖，然后通过群晖连接到内网服务器**，相当于**把群晖作为一个非常实用的跳板机**。

**个人开发者如果只有一台服务器，也不想购买各种容灾服务**，可以在服务器开一个webdav服务（Nginx就可以开），**群晖可以通过cloud sync的webdav协议，将数据定时下载到nas**；配合Hyper Backup，可以对**备份数据的历史版本进行查看**。



![Notes_1735204237000](https://cdn.fangyuanxiaozhan.com/assets/1735378630376NkYtMHZQ.jpeg)
