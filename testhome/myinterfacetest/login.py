# coding:utf-8
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json

url = 'http://212.64.19.41:9000/zentao'
r = requests.get(url)
print(r.content)

url2 = "http://212.64.19.41:9000/zentao/bug-browse-1.html"
r2 = requests.post(url2)
print(r2.content)
