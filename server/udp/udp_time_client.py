#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/5/3 --

"""
    UDP 客户端伪代码
    cs = socket()                       # 创建客户端套接字
    comm_loop:                          # 通信循环
        cs.sendto()/cs.recvfrom()       # 对话（发送/接收）
    cs.close()                          # 关闭客户端

"""
from socket import *

HOST = '127.0.0.1'
PORT = 23333
BUF_SIZE = 1024
ADDR = (HOST, PORT)

udp_client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    opt = input(">")
    if not opt:
        break
    udp_client_socket.sendto(opt.encode("utf-8"), ADDR)
    data, addr = udp_client_socket.recvfrom(BUF_SIZE)
    if not data:
        break
    print(data.decode("utf-8"))

udp_client_socket.close()
