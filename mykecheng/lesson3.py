#coding:utf-8

import requests

import time

import json

import urllib3

import re

from bs4 import BeautifulSoup

import os

urllib3.disable_warnings()

url = "https://passport.cnblogs.com/user/signin"

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}
r1 = requests.get(url, headers=headers, verify=False)
print("添加前的cookies")
print(r1.cookies)

c = requests.cookies.RequestsCookieJar()
c.set(".CNBlogsCookie", "5F1D0B9F08CDE1D0467CBFFA213F4D82332097F1E9FCF590C42E0594AA92B55946930D9177B1CF51EFDD8D640FF93F0F259E8B1E1504970567573225EC795FEAD81E798DCA6B97D24F1B3C3CCC9BB69F47635493449CBF671C1EF18478233F816D505129")
c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8J0rgDI0eRtJkfTEZKR_e80ACjSISVDHWkOlJXWV5pLTpEGhizWg--sB0Ef4rQgzY7EOtZm-joJ5xhlpwk9hu4K5gWePsiCpEMVrET123DiiqvXXL05VkV7JQTJCHORfAiW6UyoxI21bzoCTIThbkvj4ucGVotm6aCGVdNOTC4du9SOns2IGN8IRkf4WxeQM_NBNmPc1wBq4MVR8jCvU_t75IpF_6MmYOajKdPuCKL_D75PrNEtV0m-9yIDEUqhbCVtmv9ByI1jbIaSle8LS3-yFAwGi4rYwoN0om_ReXc6v')

print("添加后的cookies")
print(r1.cookies)
login_cookies = r1.cookies


url2 = " https://i.cnblogs.com/EditPosts.aspx?opt=1"

body = {"__VIEWSTATE" : "",
        "VIEWSTATEGENERATOR" : "FE27D343",
        "Editor$Edit$txbTitle" : "test222",
        "Editor$Edit$EditorBody": "<p>test2222</p>",
        "Editor$Edit$Advanced$ckbPublished": "on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments": "on",
        "Editor$Edit$Advanced$chkMainSyndication": "on",
        "Editor$Edit$Advanced$txbEntryName": "",
        "Editor$Edit$Advanced$txbExcerpt": "",
        "Editor$Edit$Advanced$txbTag": "",
        "Editor$Edit$Advanced$tbEnryPassword": "",
        "Editor$Edit$lkbDraft": "存为草稿"
        }

r2= requests.post(url2,data=body,verify=False,cookies=login_cookies)

soup = BeautifulSoup(r2.content, "html.parser")
print(soup)



