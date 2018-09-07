#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2

url = "http://www.renren.com/410043129/profile"

headers = {
    "Host" : "www.renren.com",
    "Connection" : "keep-alive",
    #"Upgrade-Insecure-Requests" : "1",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Referer" : "http://www.renren.com/SysHome.do",
    #"Accept-Encoding" : "gzip, deflate, sdch",
    "Cookie" : "anonymid=ixrna3fysufnwv; _r01_=1; depovince=GW; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484400895379; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484400890914; JSESSIONID=abcX8s_OqSGsYeRg5vHMv; jebecookies=0c5f9b0d-03d8-4e6a-b7a9-3845d04a9870|||||; ick_login=8a429d6c-78b4-4e79-8fd5-33323cd9e2bc; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=0cedb18d0982741d12ffc9a0d93670e09; ap=327550029; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg; t=56c0c522b5b068fdee708aeb1056ee819; societyguester=56c0c522b5b068fdee708aeb1056ee819; id=327550029; xnsid=5ea75bd6; loginfrom=syshome",
    "Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
}

request = urllib2.Request(url, headers = headers)

response = urllib2.urlopen(request)

print response.read()
