#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen("http://www.baidu.com/")

# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
html = response.read()

# 打印响应内容
print html
