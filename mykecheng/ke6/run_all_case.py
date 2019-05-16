#coding:utf-8

import unittest
import time
from mykecheng.ke6.common import HTMLTestRunner

import os

print(__file__)
basepath = os.path.realpath(os.path.dirname(__file__))
print(basepath)
casepath = os.path.join(basepath, "case")
reportpath = os.path.join(basepath, "report")
print(reportpath)


discover = unittest.defaultTestLoader.discover(casepath, "test*.py")
print(discover)


nowtime = time.strftime("%Y_%m_%%d_%H_%M_%S")
print(discover)

htmlpath = os.path.join(reportpath, "result.html")
print(htmlpath)

rp = open(htmlpath, "wb")

runner = HTMLTestRunner.HTMLTestRunner(rp, title="报告标题", description="报告的描述")

runner.run(discover)
