#coding=utf-8
import  requests

# response=requests.post("http://www.baidu.com/")
formatdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}
# formatdata={
# "i":"hello",
# "from":"AUTO",
# "to":"AUTO",
# "smartresult":"dict",
# "client":"fanyideskweb",
# "sign":"622c1784a848d071f9e2e4a53d093a2d",
# "doctype":"json",
# "version":"2.1",
# "keyfrom":"fanyi.web",
# "action":"FY_BY_REALTIME",
# "typoResult":"false"
# }
# url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
url="http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
# url="http://fanyi.youdao.com/"
headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response=requests.post(url,data=formatdata,headers=headers)

print response.text
# print response.json()

