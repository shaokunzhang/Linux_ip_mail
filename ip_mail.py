#-*-coding:utf-8-*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(("www.baidu.com",80))
ip_adress=s.getsockname()[0]
print (ip_adress)
