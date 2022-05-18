# debian install

https://wiki.debian.org/DebianInstaller/Preseed#Processing_templates_files

https://www.debian.org/releases/stable/example-preseed.txt

用网络版的 iso 文件启动，进入选择界面时，按 esc，到命令行窗口，输入：(回车，即可开始自动安装)

```
auto url=http://192.168.8.39/debian/preseed.txt
```

## start server

```bash
python3 -m http.server --directory debian/
```
