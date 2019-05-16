# coding:utf-8

import requests

url = 'http://hbsmz.iwin8.cc/api/auth/oauth/token?'
header = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Authorization': 'Basic cGlnOnBpZw==',
    'Content-Length': '89',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'Hm_lvt_1dfa88d0c8571eef2d383070cb3e5ca1=1557103021,1557189401,1557276719,1557362430; Hm_lpvt_1dfa88d0c8571eef2d383070cb3e5ca1=1557390851',
    'Host': 'hbsmz.iwin8.cc',
    'Origin': 'http://hbsmz.iwin8.cc',
    'Proxy-Connection': 'keep-alive',
    'Referer': 'http://hbsmz.iwin8.cc/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

body = {
    'username': 'admin',
    'password': '123456',
    'scope': 'server',
    'grant_type': 'password'
}

r = requests.post(url, json=body, headers=header)
print(r.content)



url2 = 'http://hbsmz.iwin8.cc/api/admin/entryExitHistory/page?'


body2 = {
    'current': 1,
    'size':5,
    'socialCreditNumber':'91420104616561076D',
    'name': '',
    'cellPhone': '',
    'idCardNumber': '',
    'teamSysNo': '',
    'jobType': '',
    'deviceRecord': '',
    'numbers': ''
}
