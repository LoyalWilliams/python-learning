#coding=utf-8
import json
import chardet

# 1. json.loads()
# 把Json格式字符串解码转换成Python对象 从json到python的类型
print '###################### 1. json.loads() ######################'
strList = '[1, 2, 3, 4]'
strDict = '{"city": "北京", "name": "大猫"}'

print json.loads(strList),type(json.loads(strList))
# [1, 2, 3, 4]
print json.loads(strDict),type(json.loads(strDict)) # json数据自动按Unicode存储
# {u'city': u'\u5317\u4eac', u'name': u'\u5927\u732b'}

# 2. json.dumps()
# 实现python类型转化为json字符串，返回一个str对象 把一个Python对象编码转换成Json字符串
print '######################  2. json.dumps() ######################'
listStr = [1, 2, 3, 4]
tupleStr = (1, 2, 3, 4)
dictStr = {"city": "北京", "name": "大猫"}

json.dumps(listStr)
# '[1, 2, 3, 4]'
json.dumps(tupleStr)
# '[1, 2, 3, 4]'

# 注意：json.dumps() 序列化时默认使用的ascii编码
# 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
# chardet.detect()返回字典, 其中confidence是检测精确度

print json.dumps(dictStr)
# '{"city": "\\u5317\\u4eac", "name": "\\u5927\\u5218"}'

print chardet.detect(json.dumps(dictStr))
# {'confidence': 1.0, 'encoding': 'ascii'}

print json.dumps(dictStr, ensure_ascii=False)
# {"city": "北京", "name": "大刘"}

chardet.detect(json.dumps(dictStr, ensure_ascii=False))
# {'confidence': 0.99, 'encoding': 'utf-8'}

# 3. json.dump()
# 将Python内置类型序列化为json对象后写入文件
print '######################  3. json.dump() ######################'
listStr = [{"city": "北京"}, {"name": "大刘"}]
json.dump(listStr, open("listStr.json","w"), ensure_ascii=False)

dictStr = {"city": "北京", "name": "大刘"}
json.dump(dictStr, open("dictStr.json","w"), ensure_ascii=False)

# 4. json.load()
# 读取文件中json形式的字符串元素 转化成python类型
print '######################  4. json.load() ######################'
strList = json.load(open("listStr.json"))
print strList

# [{u'city': u'\u5317\u4eac'}, {u'name': u'\u5927\u5218'}]

strDict = json.load(open("dictStr.json"))
print strDict
# {u'city': u'\u5317\u4eac', u'name': u'\u5927\u5218'}
