#coding=utf-8
import urllib2
import jsonpath
import json
import chardet

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
request =urllib2.Request(url)
response = urllib2.urlopen(request)
html = response.read()

# 把json格式字符串转换成python对象
jsonobj = json.loads(html)

# 从根节点开始，匹配name节点
citylist = jsonpath.jsonpath(jsonobj,'$..name')

print citylist
print type(citylist)
fp = open('city.json','w')

content = json.dumps(citylist, ensure_ascii=False)
print content

fp.write(content.encode('utf-8'))
fp.close()