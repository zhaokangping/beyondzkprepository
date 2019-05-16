#coding:utf-8


import re

import urllib.parse

# 编码
print(urllib.parse.quote("中文"))
# 解码
print(urllib.parse.unquote("%E4%B8%AD%E6%96%87"))

url = "http://zzk.cnblogs.com/s/blogpost?Keywords=%E4%B8%AD%E6%96%87"
print(urllib.parse.unquote(url))

url = "https://i.cnblogs.com/PostDone.aspx?postid=7900629"
