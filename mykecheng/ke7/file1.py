# coding:utf-8
import requests
from bs4 import BeautifulSoup
import os
import time

s = requests.session()
url = 'http://httpbin.org/post'

title = "这个是我的标题_%s" % str(int(time.time()))
content = "这是正文内容_%s" % str(int(time.time()))

r = requests.get("http://www.cnblogs.com")
print(r.content)

soup = BeautifulSoup(r.content, "html.parser")
