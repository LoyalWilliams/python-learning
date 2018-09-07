#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

test = "test"
password = "123456"
webserver = "192.168.21.52"

# 构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
passwordMgr = urllib2.HTTPPasswordMgrWithDefaultRealm()

# 添加授权账户信息，第一个参数realm如果没有指定就写None，后三个分别是站点IP，账户和密码
passwordMgr.add_password(None, webserver, test, password)

# HTTPBasicAuthHandler() HTTP基础验证处理器类
httpauth_handler = urllib2.HTTPBasicAuthHandler(passwordMgr)

# 处理代理基础验证相关的处理器类
proxyauth_handler = urllib2.ProxyBasicAuthHandler(passwordMgr)

# 构建自定义opener
opener = urllib2.build_opener(httpauth_handler, proxyauth_handler)

#urllib2.install_opener(opener)

request = urllib2.Request("http://192.168.21.52/")

# 用授权验证信息
response = opener.open(request)

# 没有授权验证信息
#response = urllib2.urlopen(request)

print response.read()
