---
title: 求和!李姐万岁!用ChatGPT写GitBook布局锤子便签配色的WordPress主题
tags:
- 个人成长
categories:
- 程序员折腾笔记
---



我早期在Github写《Chrome插件英雄榜》连载的时候，用的是GitBook的自动构建功能，也就是在Github仓库，按照一定的规范存储markdown格式文章和配置文件，GitBook就会自动构建一本书，供读者阅读。



GitBook阅读体验确实不错，**在PC版，左侧是目录，右侧是正文内容，点击左侧目录，就可以切换右侧的正文内容**，在移动版，目录则收到一个抽屉布局中，**点击左上角图标可以唤出抽屉，点击抽屉里的目录，可以切换主屏幕的内容**。



后来，GitBook开源版不再更新，开始专注商业付费版（限制存储空间），我于是开始寻找免费的替代品。最终选择了WordPress



WordPress是一个很成功的产品，2003年发布至今，**实现了开源与商业化的平衡**，免费版一直更新，成就了丰富的**插件**以及**主题**生态，开发者们可以通过开发WordPress**插件**或**主题**，获取收益，也可以用爱发电，发布免费的主题和插件，由于WordPress代码开源，自然也**没有类似苹果税的概念**。



**世界上三分之一的网站都由WordPress构建**，WordPress支持完整强大的后台管理，支持评论功能，支持全站搜索，搜索引擎都会对WordPress网站做优化，网站SEO变得简单！**垃圾评论过滤，评论邮件提醒，网站缓存优化，Google广告接入，提供Rss订阅等常见功能，都能通过免费稳定的插件轻松获取**。



**既要又要是人类的本性**，我切换到WordPress后，又开始**想念GitBook优秀的布局设计**，同时又想要**锤子便签一样舒适的配色阅读体验**，但没有找到现成的主题，于是我打算自己写一个，**但WordPress主题需要用到PHP语法，于是我让ChatGPT帮忙写PHP，ChatGPT写PHP很优秀，活儿好不粘人，让我有了做甲方的感觉**。

![WordPress PHP](https://cdn.fangyuanxiaozhan.com/assets/16798130107504ZC4CxAX.png)

主题写完了初版，主题暂定名称为《**求和!李姐万岁! GitBook For WordPress**》目前已经发布到 https://fangyuanxiaozhan.com  （方圆小站）运行使用，方圆小站完全由白嫖的Github Actions 运行时进行管理，管理脚本开源地址 https://github.com/zhaoolee/WordPressXMLRPCTools 脚本的目的是用Hexo的方式管理WordPress「使用Github Actions自动更新文章到WordPress」

![主题](https://cdn.fangyuanxiaozhan.com/assets/1679809887392GD20kTQs.png)

## 主题封面图

![screenshot](https://cdn.fangyuanxiaozhan.com/assets/1679809799514AP7521fB.jpeg)

## 效果演示



- 宽窄屏自适应

![Gitbook ](https://cdn.fangyuanxiaozhan.com/assets/1679811878976jke7xdWQ.gif)

如果你们的重点放在蒂法上，来这里 https://fangyuanxiaozhan.com/p/2023-01-08-13-50-22-ff7/  服务器带宽有限，图片加载稍慢，可能需要多等一会儿（如果有便宜带宽的服务器推荐，评论区可以推荐一波）

- 支持搜索

![支持搜索](https://cdn.fangyuanxiaozhan.com/assets/1679812197742NJW5ZNBE.gif)



（我觉得爱丽丝建模真不错，ff7重制版第二弹2023年赶快出！）



## 关于主题《求和!李姐万岁! GitBook For WordPress》

主题开源在Github: https://github.com/zhaoolee/gitbook-for-wordpress 

- 侧边栏按时间倒序显示已发布文章
- 目录切换文章，侧边栏自动将当前文章滚动到侧边栏顶部
- 移动端与PC端自适应布局
- 支持评论
- 支持搜索
- 底部预留备案号位置



## 后续计划的更新

- 支持按照专题自动生成多级目录
- 持续打磨样式，优化代码结构
- 写一份WordPress免费插件推荐列表



## 不要因为走的太远，就忘了当初为什么出发



![不要因为走的太远-就忘了当初为什么出发](https://cdn.fangyuanxiaozhan.com/assets/1679812767768t1FBsEQQ.png)

写博客最大的乐趣在于分享，博客应该是：**有趣想法生成器，个人项目分享器，优质内容发射器**；而不是废话连篇生成器，广告生成器，带货生成器...

在2023年，为WordPress写主题，让个人独立博客更易读易用，看起来是性价比很低的事，但按照我的折腾经验，在个人域名写独立博客，比内容平台发内容要爽的多，因为可以**写想写的内容，随时向互联网发布自己的观点**，而不是**今天发布的内容可见，明天可能就变成知识的荒原**。

《求和!李姐万岁! GitBook For WordPress》主题用了罗老师的头像做素材，最后放一句罗老师的上古语录：**希望那些喜欢用 「枪打出头鸟」 这样的道理教训年轻人，并且因此觉得自己很「成熟」的中国人有一天能够明白这样一个事实： 有的鸟来到世间，是为了做它认为正确的事，而不是专门躲枪子儿的。如果没被干掉就继续彪悍嚣张下去，如果被干掉了老子就认了**。
