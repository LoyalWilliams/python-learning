#coding=utf-8

import requests

proxies = {
  "http": "218.106.98.166:53281",
  # "https": "http://12.34.56.79:9527",
}
response = requests.get("http://www.baidu.com", proxies = proxies)
print response.text


# print "###############################################333"
# # 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
# proxy = { "http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816" }
#
# response = requests.get("http://www.baidu.com", proxies = proxy)
#
# print response.text