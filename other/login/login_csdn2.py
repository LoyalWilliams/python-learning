#coding=utf-8
import json
import requests
import time
from selenium import webdriver
from requests.cookies import RequestsCookieJar

# 保存cookie值到文本
def saveCookies(cookies):
    with open("cookies.txt", "w") as fp:
        json.dump(cookies, fp)

# 从文本中获取cookie值
def getCookies():
    with open("cookies.txt", "r") as fp:
        cookies = json.load(fp)
        return cookies

def seleniumSaveCookies(name,pwd):
    driver = webdriver.Chrome()
    url = 'https://passport.csdn.net/passport_fe/login.html'
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/ul/li[1]/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="all"]').send_keys(name)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="password-number"]').send_keys(pwd)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div[2]/form/div/div[6]/div/button').click()
    time.sleep(1)
    cookies = driver.get_cookies()
    saveCookies(cookies)
    driver.quit()

def main():
    name=raw_input('请输入账号：')
    pwd=raw_input('请输入密码：')
    seleniumSaveCookies(name,pwd)
    session = requests.session()
    # 这里我们使用cookie对象进行处理
    jar = RequestsCookieJar()
    cookies = getCookies()
    for cookie in cookies:
        jar.set(cookie['name'], cookie['value'])
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    }
    print session.cookies
    # 访问一下消息中心验证已经登录了
    print session.get('https://msg.csdn.net/', headers=headers,verify=False,cookies=jar).text
    print session.cookies

if __name__ == '__main__':
    main()