#coding=utf-8
import urllib2
from lxml import etree

def main():
    url= 'https://tieba.baidu.com/f?ie=utf-8&kw=%E7%81%AB%E5%BD%B1&fr=search'
    header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
    request=urllib2.Request(url,headers=header)
    html=urllib2.urlopen(request).read()

    #解析html为HTML文档
    selector=etree.HTML(html)
    # print selector
    links=selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
    counter = 0
    for link in links:
        img_url= 'https://tieba.baidu.com'+link
        request=urllib2.Request(img_url,headers=header)
        img_HTML=urllib2.urlopen(request).read()

        images_links= etree.HTML(img_HTML).xpath('//img[@class="BDE_Image"]/@src')


        for images_link in images_links:
            # print images_link
            request=urllib2.Request(images_link,headers=header)
            img=urllib2.urlopen(request).read()
            with open("./images/"+str(counter)+'.png',"wb") as f:
               f.write(img)
            counter+=1
            print counter
        #最多爬30多张图片
        if (counter>=30):
            break




if __name__ == '__main__':
    main()


