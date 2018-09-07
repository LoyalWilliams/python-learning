#!/usr/bin/env python
# -*- coding:utf-8 -*-


import re
pattern = re.compile(r'\d+')  # 用于匹配至少一个数字

m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
print m

m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print m

m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print m                                         # 返回一个 Match 对象

print m.group(0)   # 可省略 0

print m.start(0)   # 可省略 0

print m.end(0)     # 可省略 0

print m.span(0)    # 可省略 0