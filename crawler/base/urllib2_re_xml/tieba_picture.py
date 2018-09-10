#coding=utf-8
import urllib2
from lxml import etree

def main():
    url= 'https://tieba.baidu.com/f?kw=%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85&ie=utf-8'
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    request=urllib2.Request(url,headers=header)
    html=urllib2.urlopen(request).read()

    #解析html为HTML文档
    selector=etree.HTML(html)
    # 结果返回的是一个列表
    links=selector.xpath('//img[@class="card_head_img"]/@src')
    print links[0]
    request = urllib2.Request(links[0], headers=header)
    img = urllib2.urlopen(request).read()
    # wb表示写成二进制文件
    with open("./images/head_img.jpg","wb") as file:
        file.write(img)





if __name__ == '__main__':
    main()
