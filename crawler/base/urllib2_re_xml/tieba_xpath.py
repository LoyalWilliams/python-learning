#coding=utf-8
import urllib2
import urllib
from lxml import etree

def main():
    url= 'http://tieba.baidu.com/f?ie=utf-8&kw=%E7%BE%8E%E5%A5%B3&fr=search'
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    request=urllib2.Request(url,headers=header)
    html=urllib2.urlopen(request).read()

    #解析html为HTML文档
    selector=etree.HTML(html)
    print selector


if __name__ == '__main__':
    main()


