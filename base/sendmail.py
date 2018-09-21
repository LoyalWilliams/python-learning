#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


sendFrom='2541692705@qq.com' #发件人邮箱账号，为了后面易于维护，所以写成了变量
sendTo='2541692705@qq.com' #收件人邮箱账号，为了后面易于维护，所以写成了变量
passwd="xwuqdsavrabqdhhf" #授权码
msg="hello" #要发送的信息内容
def mail(sendFrom,sendTo,passwd,msg):
    '''
    发送邮件的方法
    :param sendFrom: 发送人邮箱
    :param sendTo: 收件人邮箱
    :param passwd: 发送邮箱授权码
    :param msg: 发送信息
    :return:
    '''
    msg=MIMEText(msg,'plain','utf-8')
    msg['From']=formataddr(["发件人邮箱昵称",sendFrom])   #括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["mylove",sendTo])   #括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="我是邮件标题" #邮件的主题，也可以说是标题
    server=smtplib.SMTP("smtp.qq.com",25)  #发件人邮箱中的SMTP服务器，端口是25
    server.login(sendFrom,passwd)    #括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(sendFrom,[sendTo,],msg.as_string())   #括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()   #这句是关闭连接的意思

mail(sendFrom,sendTo,passwd,msg)
