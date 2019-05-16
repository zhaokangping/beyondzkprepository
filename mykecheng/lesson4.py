#coding:utf-8

import time

import requests

title = "这是标题_%s" % str(int(time.time()))
content = "正文内容_%s" % str(int(time.time()))


url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"

s = requests.session()

print("更新之前的cookies:%s" % s.cookies)

c = requests.cookies.RequestsCookieJar()
c.set(".CNBlogsCookie", "5F1D0B9F08CDE1D0467CBFFA213F4D82332097F1E9FCF590C42E0594AA92B55946930D9177B1CF51EFDD8D640FF93F0F259E8B1E1504970567573225EC795FEAD81E798DCA6B97D24F1B3C3CCC9BB69F47635493449CBF671C1EF18478233F816D505129")
c.set('.Cnblogs.AspNetCore.Cookies', 'CfDJ8J0rgDI0eRtJkfTEZKR_e80ACjSISVDHWkOlJXWV5pLTpEGhizWg--sB0Ef4rQgzY7EOtZm-joJ5xhlpwk9hu4K5gWePsiCpEMVrET123DiiqvXXL05VkV7JQTJCHORfAiW6UyoxI21bzoCTIThbkvj4ucGVotm6aCGVdNOTC4du9SOns2IGN8IRkf4WxeQM_NBNmPc1wBq4MVR8jCvU_t75IpF_6MmYOajKdPuCKL_D75PrNEtV0m-9yIDEUqhbCVtmv9ByI1jbIaSle8LS3-yFAwGi4rYwoN0om_ReXc6v')

s.cookies.update(c)
print("更新之后的cookies:%s" % s.cookies)

url2 = s.get("https://i.cnblogs.com/EditPosts.aspx?opt=1",verify=False)
print(url2.text)
