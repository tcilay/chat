#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/5/3 --

"""
    UDP服务器伪代码
    ss = socket()                           # 创建服务器套接字
    ss.bind()                               # 绑定服务器套接字
    inf_loop:                               # 服务器无限循环
        cs = ss.recvfrom()/ss.sendto()      # 关闭（接收/发送）
    ss.close()                              # 关闭服务器套接字

"""
from socket import *
from time import ctime

HOST = ''
PORT = 23333
BUF_SIZE = 1024
ADDR = (HOST, PORT)

udp_server_socket = socket(AF_INET, SOCK_DGRAM)
udp_server_socket.bind(ADDR)

while True:
    print(" waiting for message ...")
    data, addr = udp_server_socket.recvfrom(BUF_SIZE)
    if not data:
        break
    udp_server_socket.sendto(('[%s] %s' % (ctime(), data.decode("utf-8"))).encode("utf-8"), addr)
    print("... received from and returned to:", addr)

udp_server_socket.close()
