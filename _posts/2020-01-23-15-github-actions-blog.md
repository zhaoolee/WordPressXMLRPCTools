---
title: 使用Github Actions 动态更新Github主页
tags: 
- github
- Github Action
categories:
- 程序员折腾笔记
---

我在Github的用户名为zhaoolee，如果我在Github中建立一个名为zhaoolee的仓库，那zhaoolee仓库中READNE.md的内容，便会展现到github主页顶部。更有趣的是，如果给仓库编写一个脚本，就可以利用Github Actions自动更新主页的内容。

我有两个网站**V2方圆**和**方圆小站**，我通过Github Actions设置了一个每隔15分钟自动运行的任务，任务内的程序会自动爬取**V2方圆**和**方圆小站**的前三篇内容，并将链接更新到我的Github主页。当用免费的Github Actions为自己的博客引流时，我体会到了白嫖的快乐，获得了Github长期的优质流量。

![image](https://cdn.fangyuanxiaozhan.com/assets/1611388991979Mkpibtet.png)

####  Python脚本如下

```python
import feedparser
import time
import os
import re
import pytz
from datetime import datetime

def get_link_info(feed_url, num):
    result = ""
    feed = feedparser.parse(feed_url)
    feed_entries = feed["entries"]
    feed_entries_length = len(feed_entries)
    all_number = 0;
    if(num > feed_entries_length):
        all_number = feed_entries_length
    else:
        all_number = num
    
    for entrie in feed_entries[0: all_number]:
        title = entrie["title"]
        link = entrie["link"]
        result = result + "\n" + "[" + title + "](" + link + ")" + "\n"
    return result
    
def main():
    v2fy_info =  get_link_info("https://v2fy.com/feed/", 3)
    fangyuanxiaozhan_info =  get_link_info("https://fangyuanxiaozhan.com/feed/", 3)
    insert_info = v2fy_info + fangyuanxiaozhan_info
    # 替换 ---start--- 到 ---end--- 之间的内容
    # pytz.timezone('Asia/Shanghai')).strftime('%Y年%m月%d日%H时M分')
    fmt = '%Y-%m-%d %H:%M:%S %Z%z'
    insert_info = "---start---\n\n## 最近更新文章(" + "更新时间:"+  datetime.fromtimestamp(int(time.time()),pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S') + " | 通过Github Actions自动更新)" +"\n" + insert_info + "\n---end---"
    # 获取README.md内容
    with open (os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()
    new_readme_md_content = re.sub(r'---start---(.|\n)*---end---', insert_info, readme_md_content)
    with open (os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)
main()
```



#### 以上代码以及Github Action配置文件永久开源地址

[https://github.com/zhaoolee/zhaoolee](https://github.com/zhaoolee/zhaoolee)



Github Actions脚本位置:

[https://github.com/zhaoolee/zhaoolee/edit/main/.github/workflows/main.yml](https://github.com/zhaoolee/zhaoolee/edit/main/.github/workflows/main.yml)



#### 如果大家都善用Github自定义主页，互联网会更开放


长期来看，Github在搜索引擎中的权重很高，以上方法直接为搜索引擎提供最新的内容资源，如果推广开来，会让互联网更开放，而不是内容平台各自跑马圈地，割裂互联网。虽然真正开放的互联网很难达成，但我还是想，留给后来者一个尽可能开放的，资源知识一触及达的互联网。


Github Actions玩法是丰富多彩的，道路也是曲折渐进的，关于定时任务，阮一峰大佬，搞了一个定时往自己邮箱发天气预报的功能; 以前有一个表特日报的服务，订阅后，每日都能收到ptt网站最新的好看妹子图片, 我们也可以把发天气预报搞成公共服务，需要的人只需在仓库issues下留下自己的邮箱，程序会定时获取issues内的邮箱，然后群发，这样大家都能享受天气预报的邮件服务。

#### Gihub Actions的不足


Github Actions 也还有一些小bug，如果你设置每隔15分钟运行一次，可能会偶尔漏掉几次任务，目前比较好的解决方案是，把频次改成每2小时发一次，基本可以避免漏发（Github Actions应该是资源不足造成的，微软有的是银子，多氪金就能修复）
