---
title: GitBook锤子便签风格WordPress主题目录设计思想
tags:
- 个人成长
categories:
- 程序员折腾笔记
---



最近在进行锤子便签风格WordPress主题 《求和!李姐万岁! GitBook For WordPress》的开发, WordPress支持对文章进行**分类**（Category），非常适合写长期连载。

[开源地址: https://github.com/zhaoolee/gitbook-for-wordpress](开源地址: https://github.com/zhaoolee/gitbook-for-wordpress)

我设计左侧目录的核心思想是: **左侧目录默认展示所有分类的内容，列表内容按照时间进行倒序，如果使用分类，则将分类信息增强同步到url**

## 列表排序按时间倒序

Gitbook要求用户自己写目录，与我而言, 过于麻烦了，**大多数情况下，沿用时间轴的思路，直接倒序即可**，WordPress是有数据库的全功能网站，如果对排序不满意，可以后台手动调整发布时间。

![image-20230330194612331](https://cdn.fangyuanxiaozhan.com/assets/1680176773879d1XF1Nh3.png)



## 追加url参数，按照「分类」过滤



![分类](https://cdn.fangyuanxiaozhan.com/assets/168017795183958AJ4x33.png)

如果我们选择了某个分类，则分类列表里面的文章尾部会追加一个post_category参数，这样做有两个好处

**第一：非破坏性**；追加的post_category 不会破坏已有的路由规则 , 如果url不包含post_category参数，则默认进入「全部分类」

**第二：一键过滤专题文章**：如果追加的post_category的值为「Chrome插件英雄榜」，则左侧Select组件会默认选中「Chrome插件英雄榜」，左侧列表的内容全部为「Chrome插件英雄榜」系列的文章; 在选择「Chrome插件英雄榜」的状态下，列表里文章url都会被自动追加 post_category=Chrome插件英雄榜 , 这样在url追加专题名称的做法，也有助于SEO，分享出去的文章url 链接追加post_category=Chrome插件英雄榜， 也有助于打开链接的人，一眼看到左侧列表整个专题的文章


![追加参数](https://cdn.fangyuanxiaozhan.com/assets/1680177020865FKhMp0z6.png)

参考Gitbook左侧列表做减法：**Gitbook通过多级目录进行分类，左侧列表无法根据分享的url直接滚动定位**（不同层级的高度不同，还有复杂的父子折叠态，gitbook直接放弃了通过url滚动定位左侧目录列表）, 我采用最简单的一级目录，实现了左侧列表的精准滚动定位，**通过url自动过滤的方式，消除其它专题对用户的视觉干扰**。


## 小结

无论是程序设计，还是个人项目，**借鉴好作品，做减法，才会做出符合需求的优秀成品**。

GitBook层级目录很适合做文档，我的需求是按照专题长期写连载博客;，用Select选择专题, 过滤文章列表，然后按照发布时间自动反向排序，是我目前实现的最优策略。

