echo -n  "请输入文件名 ->"
read  filename
touch  ./_posts/$(date "+%Y-%m-%d-%H-%M-%S-$filename.md")
