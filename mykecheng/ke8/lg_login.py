#coding:utf-8

import requests
from bs4 import BeautifulSoup
import re

s = requests.session()

def get_token(s):
    url = 'passport.lagou.com/login/login.html'
    h = {
        'User - Agent':
        'Mozilla / 5.0(Macintosh;IntelMacOSX10_13_2) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3497.100Safari / 537.36'
    }
    r1 = s.get(url, headers=h, verify=False)
    print(r1.text)


    soup = BeautifulSoup(r1.content,"html.parser", from_encoding='utf-8')
    tokenCode = {}
    try:
        t = soup.find_all('script')[1].get_text()
    except:


        
