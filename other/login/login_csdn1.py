#coding=utf-8
import json
import requests

def main():
    name=raw_input('请输入账号：')
    pwd=raw_input('请输入密码：')
    data = {"loginType": "1", "pwdOrVerifyCode": pwd, "userIdentification": name}

    jsontext=json.dumps(data)
    print jsontext
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    }
    url='https://passport.csdn.net/v1/register/pc/login/doLogin'
    session=requests.session()
    response = session.post(url, data=jsontext, headers=headers, verify=False)
    print response.text
    print session.get('https://msg.csdn.net/', headers=headers,verify=False).text

if __name__ == '__main__':
    main()