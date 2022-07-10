echo "请输入文件名 ->"
read -e filename
touch  ./_posts/$(date "+%Y-%m-%d-%H-%M-%S-$filename.md")
echo "---
title: $filename 
tags:
- 个人成长
categories:
- 杂谈
---\n" > ./_posts/$(date "+%Y-%m-%d-%H-%M-%S-$filename.md")
