#coding=utf-8
import time
from selenium import webdriver
import requests
import json
import sys
import codecs

class qqGroupSpider():
    '''
    Q群爬虫类
    '''
    def __init__(self, qq,passwd):
        self.qqGroupCount=0
        self.nextCount=0
        self.members=[]
        self.qqGroupNum=0
        url = "https://qun.qq.com/member.html"
        driver = webdriver.Chrome()
        driver.delete_all_cookies()
        driver.get(url)

        time.sleep(1)
        driver.switch_to.frame("login_frame")  # 进入登录iframe
        time.sleep(1)
        change = driver.find_element_by_id("switcher_plogin")
        change.click()
        driver.find_element_by_id('u').clear()  # 选择用户名框
        driver.find_element_by_id('u').send_keys(qq)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(passwd)
        driver.find_element_by_class_name("login_button").click()

        time.sleep(3)
        self.skey = driver.get_cookie('skey')['value']
        self.p_skey = driver.get_cookie('p_skey')['value']
        self.cookie = "uin=o" + qq + "; skey=" + self.skey + "; p_skey=" + self.p_skey
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
            "Cookie": self.cookie
        }
        e = self.skey
        t = 5381
        for n in range(0, len(e)):
            t += (t << 5) + ord(e[n])
            t &= sys.maxint
        self.bkn = t
        driver.quit()

    class Mylist():
        '''
        自定义列表，自定义迭代器
        '''
        def __init__(self,members,qqGroupNum,qqGroupCount):
            self.nextCount=0
            self.qqGroupCount=qqGroupCount
            self.qqGroupNum=qqGroupNum
            self.members=members
            self.spider=None

        def __iter__(self):
            return self

        def next(self):
            if self.nextCount >= self.qqGroupCount:
                raise StopIteration
            elif self.nextCount==0:
                self.nextCount += 1
                return self.members[0]
            elif (self.nextCount)%100==0:
                members = self.spider.getMembers(self.qqGroupNum,start=self.nextCount)
                self.members=members
                self.nextCount += 1
                return members[0]
            else:
                self.nextCount += 1
                return self.members[(self.nextCount-1)%100]

    def getGroupList(self):
        '''
        获取QQ对应的所有Q群号
        :return:
        '''
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
            "Cookie": self.cookie
        }

        groupInfoR = requests.post('https://qun.qq.com/cgi-bin/qun_mgr/get_group_list', data='bkn=' + str(self.bkn),
                                   headers=headers, verify=False)
        groupInfo = json.loads(groupInfoR.text)
        groupList = groupInfo['create'] + groupInfo['join']
        return groupList

    def getMembers(self,qqGroupNum,start=0,count=100):
        '''
        获取Q群成员列表的方法，返回json数组
        :param qqGroupNum: Q群号
        :param start: Q群成员的开始下标索引
        :param count: 获取Q群成员的个数，默认取100个，不足100个成员，则全部取出
        :return: 返回Q群成员列表
        '''
        self.qqGroupNum=qqGroupNum
        data = {'gc': qqGroupNum, 'st': start, 'end': start+count, 'sort': 0, 'bkn': self.bkn}
        response = requests.post("https://qun.qq.com/cgi-bin/qun_mgr/search_group_members", data=data, headers=self.headers,
                                 verify=False)
        qqJson = json.loads(response.text)
        self.qqGroupCount = qqJson['count']
        members = qqJson['mems']
        return members

    def getMembers2(self, qqGroupNum):
        '''
        返回一个自定义的列表，列表可以返回QQ成员信息
        :param qqGroupNum: Q群号
        :return:
        '''
        self.qqGroupNum = qqGroupNum
        data = {'gc': qqGroupNum, 'st': 0, 'end': 100, 'sort': 0, 'bkn': self.bkn}
        response = requests.post("https://qun.qq.com/cgi-bin/qun_mgr/search_group_members", data=data,
                                 headers=self.headers,
                                 verify=False)
        qqJson = json.loads(response.text)
        count = qqJson['count']
        members = qqJson['mems']
        mylist=self.Mylist(members, qqGroupNum, count)
        mylist.spider=self
        return mylist

def main():
    qq=raw_input('请输入QQ号：')
    pwd=raw_input('请输入密码：')
    spider=qqGroupSpider(qq,pwd)
    groupList =spider.getGroupList()

    print '请选择以下Q群进行爬取'
    for each in groupList:
        print each['gn'],":",each['gc']
    qqGroup=raw_input('请输入Q群号：')

    members =spider.getMembers2(qqGroup)
    # members=spider.getMembers(qqGroup)

    writefile = codecs.open(u'qqGroup.txt', 'w',encoding='utf-8')
    writefile.write(u'昵称,q号,性别,q龄,入群时间,等级(积分),最后发言\n')
    for one in members:
        lv=one['lv']
        g=one['g']
        gender=u'男'
        if g==255:
            gender=u'未知'
        elif g==0:
            pass
        elif g==1:
            gender=u'女'
        else:
            gender=g

        join_time = time.localtime(one['join_time'])
        join_time = str(join_time[0]) + u'年' + str(join_time[1]) + u'月' + str(
            join_time[2]) + u'日' + str(join_time[3]) + u'时' + str(join_time[4]) + u'分'
        last_speak_time = time.localtime(one['last_speak_time'])
        last_speak_time=str(last_speak_time[0]) + u'年' + str(last_speak_time[1]) + u'月' + str(last_speak_time[2]) + u'日' + str(last_speak_time[3]) + u'时' + str(last_speak_time[4]) + u'分'
        datatext = one['nick']+","+str(one['uin'])+","+gender+","+str(one['qage'])+","+join_time+","+\
              str(lv['level'])+'('+str(lv['point'])+')'+","+last_speak_time+'\n'
        writefile.write(datatext)
    writefile.close()

if __name__ == '__main__':
    main()