#coding=utf-8

from bs4 import BeautifulSoup

html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建BeautifulSoup对象
soup=BeautifulSoup(html,'lxml')

'''
遍历文档树
1. 直接子节点 ：.contents .children 属性
.content
tag 的 .content 属性可以将tag的子节点以列表的方式输出
'''
print soup.head.contents
#[<title>The Dormouse's story</title>]
"""
.children
它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
我们打印输出 .children 看一下，可以发现它是一个 list 生成器对象
"""
print soup.head.children
#<listiterator object at 0x7f71457f5710>
print '################## soup.head.children ####################'
for child in  soup.body.children:
    print child

# 2. 所有子孙节点: .descendants 属性
print '######################### .descendants 属性 #################################'
for child in soup.descendants:
    print child

# 3. 节点内容: .string 属性
# 如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容。例如：
print '######################## .string 属性 ################################################'
print soup.head.string
#The Dormouse's story
print soup.title.string
#The Dormouse's story

