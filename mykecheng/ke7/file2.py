#coding:utf-8
from bs4 import BeautifulSoup
import requests
import os

# r = requests.get("https://www.qiushibaike.com/", verify=False)
# soup = BeautifulSoup(r.content, "html.parser")
# duanzi = soup.find_all(class_="content")
# for i in duanzi:
#     print(i.span.get_text().replace("\n", ""))


r2 = requests.get("http://699pic.com/sousuo-218808-13-1.html")
# print(r2.content)
soup = BeautifulSoup(r2.content, "html.parser")
# print(soup)
images = soup.find_all(class_='lazy')
curPath = os.path.dirname(os.path.realpath(__file__))
for i in images:
    try:
        jpg_url = i["data-original"]
        title = i["title"]
        print(jpg_url)
        print(title)
        with open(curPath+"\\"+title+".jpg","wb") as f:
            f.write(requests.get(jpg_url).content)
    except Exception as msg:
        print(msg)
