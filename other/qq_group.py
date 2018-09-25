#coding=utf-8
from lxml import etree
import time
from selenium import webdriver

class qqGroupSpider():
    '''
    Q群爬虫类
    '''
    def __init__(self, driver,qq,passwd,qqgroup,writefile):
        '''
        初始化根据用户信息登录到Q群管理界面
        :param driver:
        :param qq:
        :param passwd:
        :param qqgroup:
        :param writefile:
        '''
        url = "https://qun.qq.com/member.html#gid=" + str(qqgroup)
        self.writefile=writefile
        self.driver=driver
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
        time.sleep(1)

    def scroll_foot(self,driver):
        '''
        控制屏幕向下滚动一下
        :param driver:
        :return:
        '''
        js = "var q=document.documentElement.scrollTop=100000"
        return driver.execute_script(js)

    def getTbodyList(self, driver):
        return driver.find_elements_by_xpath('//div[@class="group-memeber"]//tbody[contains(@class,"list")]')

    def parseMember(self, mb):
        '''
        解析每个人各项描述，以逗号隔开，返回一个成员的基本情况
        :param mb:
        :return:
        '''
        master = mb.getchildren()[2].getchildren()[0].get('class')
        if master == None:
            master = '0'
        else:
            master = '1'
        qId = mb.getchildren()[1].text.strip()
        nickName = mb.getchildren()[2].getchildren()[2].text.strip()
        card = mb.getchildren()[3].getchildren()[0].text.strip()
        qq = mb.getchildren()[4].text.strip()
        sex = mb.getchildren()[5].text.strip()
        qqAge = mb.getchildren()[6].text.strip()
        joinTime = mb.getchildren()[7].text.strip()
        lastTime = mb.getchildren()[8].text.strip()
        return (
        master + "," + qq + "," + nickName + "," + card + "," + sex + "," + qqAge + "," + joinTime + "," + lastTime).encode(
            'utf-8')

    def parseTbody(self, html):
        '''
        解析tbody里面的内容，一个tbody里面有多个成员，
        解析完成后，返回成员基本情况的列表
        :param html:
        :return:
        '''
        selector = etree.HTML(html)
        mbs = selector.xpath('//tr[contains(@class,"mb mb")]')
        memberList = map(self.parseMember, mbs)
        return memberList

    def parseAndWrite(self, tbody):
        '''
        解析HTML中的tbody，解析完成后写入到本地文件
        :param tbody:
        :return:
        '''
        html = tbody.get_attribute('innerHTML')
        memberList = self.parseTbody(html)
        map(lambda x: self.writefile.write(x + '\n'), memberList)



def main():
    # filename = driver.find_element_by_xpath('//*[@id="groupTit"]').text.encode('utf-8').strip()
    # file = open(unicode('qq/' + filename.replace('/', '').replace('\\', '') + '.txt', 'utf-8'), 'w')
    qq = str(raw_input("请输入你的QQ:"))
    passwd = str(raw_input("请输入你的QQ密码:"))
    qqgroup = raw_input("请输入QQ群号:")
    filename = str(raw_input("请输入保存的文件名:"))
    # 保存在qq目录下，没有需要先创建
    file = open(unicode('qq/' + filename+ '.txt', 'utf-8'), 'w')
    driver = webdriver.Chrome()
    spider=qqGroupSpider(driver,qq,passwd,qqgroup,file)
    # 找到QQ群的人数
    qqNum = int(driver.find_element_by_xpath('//*[@id="groupMemberNum"]').text.strip())
    curren_qq_num=0
    count=0
    prelen=0
    while curren_qq_num != qqNum:
        # 不停的向下滚动屏幕，直到底部，一边抽取数据
        count = count+1
        print count
        spider.scroll_foot(driver)
        time.sleep(1)
        curren_qq_num=len(driver.find_elements_by_xpath('//*[@id="groupMember"]//td[contains(@class,"td-no")]'))
        tlist = spider.getTbodyList(driver)
        map(spider.parseAndWrite, tlist[prelen:])
        prelen = len(tlist)#更新tbody列表的长度
    driver.quit()
    file.close()

if __name__ == '__main__':
    main()
