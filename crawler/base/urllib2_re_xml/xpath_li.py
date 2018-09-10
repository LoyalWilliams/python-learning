#coding=utf-8
from lxml import  etree

html=etree.parse('hello.html')
print type(html)

# 1. 获取所有的 <li> 标签
print '################# 1 ################'
result=html.xpath('//li')

print 'result:',result
print len(result)
print type(result)
print type(result[0])

# 2. 继续获取<li> 标签的所有 class属性
print '################# 2 ################'
result=html.xpath('//li/@class')
print 'class:',result

# 3. 继续获取<li>标签下hre 为 link1.html 的 <a> 标签
print '################# 3 ################'
result = html.xpath('//li/a[@href="link1.html"]')
print 'a:',result

# 4. 获取<li> 标签下的所有 <span> 标签
#result = html.xpath('//li/span')
#注意这么写是不对的：
#因为 / 是用来获取子元素的，而 <span> 并不是 <li> 的子元素，所以，要用双斜杠
print '################# 4 ################'
result=html.xpath('//li//span')
print 'span:',result

# 5. 获取 <li> 标签下的<a>标签里的所有 class
print '################# 5 ################'
result=html.xpath('//li/a//@class')
print 'a:class:',result

# 6. 获取最后一个 <li> 的 <a> 的 href
print '################# 6 ################'
result=html.xpath('//li[last()]/a/@href')
print 'last:',result

# 7. 获取倒数第二个元素的内容
print '################# 7 ################'
result = html.xpath('//li[last()-1]/a')
# text 方法可以获取元素内容
print result[0].text

# 8. 获取 class 值为 bold 的标签名
print '################# 8 ################'
result = html.xpath('//*[@class="bold"]')
# tag方法可以获取标签名
print result[0].tag