#-*-coding:utf-8-*-
import socket
import time
import smtplib
import urllib
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.text import MIMEText

def sendEmail():#发送邮件
    def _format_addr(s):
      name,addr=parseaddr(s)
      return formataddr((Header(name,'utf-8').encode(),addr))

    from_addr="******@163.com"#在这里填入发件人的邮箱
    password="******"#发件人的邮箱密码
    to_addr="******@.com"#收件人的邮箱
    smtp_server="smtp.163.com"#发邮件的邮箱的服务器地址
    msg=MIMEText('IP是:'+ip_addres+'','plain','utf-8')
    msg['From']=_format_addr('raspberry pi mode 3<%s>'%from_addr)
    msg['To']=_format_addr('admin<%s>'%to_addr)
    msg['Subject']=Header('来自您的Linux','utf-8').encode()

    server=smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(1)
    server.login(from_addr,password)
    server.sendmail(from_addr,[to_addr],msg.as_string())
    server.quit()
def get_ip():#获取IP
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ip_adress=s.getsockname()[0]
    s.close()
    return ip_adress
if __name__=='__main__':
    ip_addres=get_ip()
    sendEmail()
~                  
