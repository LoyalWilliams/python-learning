#coding=utf-8
from lxml import etree

#读外部文件 hello.html
html=etree.parse('./hello.html')
result=etree.tostring(html,pretty_print=True)

print result