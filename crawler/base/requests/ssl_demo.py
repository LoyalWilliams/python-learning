#coding=utf-8

import requests
response = requests.get("https://www.baidu.com/", verify=True)

# 也可以省略不写
# response = requests.get("https://www.baidu.com/")
print response.text


print '######################################'
###### 12306证书验证要设置False否则报错
import requests
response = requests.get("https://www.12306.cn/mormhweb/",verify=False)
print response.text