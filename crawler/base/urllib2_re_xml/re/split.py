#coding=utf-8

import re
####################  split  ########################
print '####################  split  ########################'
p = re.compile(r'[\s\,\;]+')
print p.split('a,b;; c   d')

###################  sub ############################
print '###################  sub ############################'
p=re.compile(r'(\w+) (\w+)')# \w = [A-Za-z0-9]
s='hello 123,hello 456'

print s
print p.sub(r'hello world',s)       #直接替换
print p.sub(r'hello world',s,1)       #只替换一次
print p.sub(r'\2 \1',s)             #引用分组

def func(m):
    return 'hi' + '' + m.group(2)

print  p.sub(func,s,1)       #只替换一次
print  p.sub(func,s)

################### 匹配中文 #########################
print '################### 匹配中文 #########################'
title = u'你好，hello，世界'
pattern = re.compile(ur'[\u4e00-\u9fa5]+')
result = pattern.findall(title)

print result
print result[0],result[1]


