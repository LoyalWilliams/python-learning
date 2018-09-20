#coding=utf-8
import urllib2
import urllib
from lxml import etree
import re

import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr


sendFrom='loyalwilliams@163.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
sendTo='2541692705@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
passwd="" #密码
msg='''
java入门宝典上篇
链接：https://pan.baidu.com/s/1dzdKGCDN3jBxKEx7k-zh9Q 密码：egq3
java入门宝典下篇
链接：https://pan.baidu.com/s/14jFWo5LL4qVBj7vvICRZyg 密码：2d8o
Linux入门教程
链接：https://pan.baidu.com/s/1Fs4yKixRq-ByP5BRVHYRgw 密码：48oi
hadoop学习宝典
链接：https://pan.baidu.com/s/14NRKwJbiLKKiJxEeMg5TKQ 密码：xe8j
欢迎领走学习资料，进群学习
群主QQ：2541692705
Q群：882855741
群主博客：https://blog.csdn.net/a_hui_tai_lang
邮箱：loyalwilliams@163.com
快捷通道点击链接加入群聊【大数据学习交流群】：https://jq.qq.com/?_wv=1027&k=5B8uVZZ

        '''
def mail(sendFrom,sendTo,passwd,msg):
    '''
    发送邮件的方法
    :param sendFrom: 发送人邮箱
    :param sendTo: 收件人邮箱
    :param passwd: 发送邮箱密码
    :param msg: 发送信息
    :return: 
    '''
    ret=True
    try:
        msg=MIMEText(msg,'plain','utf-8')
        msg['From']=formataddr(["大数据学习交流",sendFrom])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["mylove",sendTo])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="大数据学习资料" #邮件的主题，也可以说是标题
        server=smtplib.SMTP("smtp.163.com",25)  #发件人邮箱中的SMTP服务器，端口是25
        server.login(sendFrom,passwd)    #括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sendFrom,[sendTo,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()   #这句是关闭连接的意思
    except Exception:   #如果try中的语句没有执行，则会执行下面的ret=False
        ret=False
    return ret


class Spider():
    '''
    贴吧爬虫类
    '''
    def __init__(self):
        self.tiebaName = raw_input("请输入需要访问的贴吧：")
        self.beginPage = int(raw_input("请输入起始页："))
        self.endPage = int(raw_input("请输入终止页："))

        # 邮箱匹配规则
        self.pattern = re.compile(r'\d+@qq.com')
        self.url = 'http://tieba.baidu.com/f'
        self.ua_header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

    def tiebaSpider(self):
        '''
        爬取贴吧所有帖子的链接
        :return: 所有帖子的链接列表
        '''
        for page in range(self.beginPage, self.endPage + 1):
            pn = (page - 1) * 50  # page number
            word = {'pn': pn, 'kw': self.tiebaName}

            word = urllib.urlencode(word)  # 转换成url编码格式（字符串）
            myUrl = self.url + "?" + word

            # 示例：http://tieba.baidu.com/f? kw=%E7%BE%8E%E5%A5%B3 & pn=50
            # 调用 页面处理函数 load_Page
            # 并且获取页面所有帖子链接,
            selector = self.loadPage(myUrl)  # urllib2_test3.py
            #  先爬取每个贴吧帖子的连接地址
            links = selector.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
            # 每个帖子的链接=基本url拼上相对路径
            return map(lambda x:"https://tieba.baidu.com"+x,links)

    # 读取页面内容
    def loadPage(self, url):
        '''
        加载url,返回xpath选择器
        :param url: 
        :return: 
        '''
        req = urllib2.Request(url, headers = self.ua_header)
        html = urllib2.urlopen(req).read()
        # 解析html 为 HTML 文档
        selector=etree.HTML(html)
        # print html
        return selector

    def emailSpider(self,url):
        '''
        爬取url内的所有qq邮箱
        :param url: 
        :return: qq邮箱列表
        '''
        request = urllib2.Request(url, headers=self.ua_header)
        content_html = urllib2.urlopen(request).read()
        # print content_html
        return self.pattern.findall(content_html)


def sendMail(sendFrom, sendTo, passwd, msg, tryTimes=3):
    '''
    发送邮件,发送失败会重新发送，默认最多尝试3次
    :param sendFrom: 
    :param sendTo: 
    :param passwd: 
    :param msg: 
    :param tryTimes: 
    :return: 
    '''
    for i in range(1, tryTimes+1):  #
        ret = mail(sendFrom, sendTo, passwd, msg)
        if ret:
            print("ok,邮件发送成功")  # 如果发送成功则会返回ok，稍等20秒左右就可以收到邮件
            break
        else:
            print("失败第[" + i + "/"+tryTimes+"]次,尝试重新发送")  # 如果发送失败则会返回filed


def main():
    spider = Spider()
    # 返回一个贴吧帖子的链接列表
    links = spider.tiebaSpider()

    for link in links:
        mails = spider.emailSpider(link)
        for qqMail in mails:
            print qqMail
            # sendMail(sendFrom, qqMail, passwd, msg)


if __name__ =="__main__":
    main()

'''
测试爬虫的方法
'''
def testSpider():
    spider=Spider()
    # spider.loadPage("https://tieba.baidu.com/f?kw=hadoop&ie=utf-8&pn=50")
    # print spider.tiebaSpider()
    emailList=spider.emailSpider("https://tieba.baidu.com/p/5793741948")
    print type(emailList),emailList
# testSpider()
