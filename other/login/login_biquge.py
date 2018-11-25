#coding=utf-8
import requests

def main():
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    }
    # 笔趣阁的登录请求接口
    url='http://www.biquge.com.tw/login.php?do=submit&action=login&usecookie=1&jumpurl='
    # 需求用的的请求数据
    data = {'username': 'a_hui_tai_lang', 'password': 'a_hui_tai_lang'}
    session=requests.session()
    response = session.post(url, data=data, headers=headers,verify=False)
    # 查看一下是否成功登录
    print response.content.decode('gbk')
    # cookies里面已经有登陆信息了
    print session.cookies

if __name__ == '__main__':
    main()
