#coding:utf-8

import requests

url = "https://www.kuaidi.com/index-ajaxselectcourierinfo-3102060429437-yunda.html"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}


s = requests.session()
r = s.get(url, headers=headers, verify=False)
result = r.json()
print(result)

print(result['companytype'])
