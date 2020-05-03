#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/5/3 --

"""
    TCP 客户端伪代码
    cs = socket()               # 创建客户端套接字
    cs.connect()                # 尝试连接服务器
    comm_loop:                  # 通信循环
        cs.send()/cs.recv()     # 对话（发送/接收）
    cs.close()                  # 关闭客户端套接字
"""
from socket import *

HOST = "127.0.0.1"
PORT = 23333
BUF_SIZE = 1024
ADDR = (HOST, PORT)

tcp_client_socket = socket(AF_INET, SOCK_STREAM)
tcp_client_socket.connect(ADDR)

while True:
    opt = input(">")
    if not opt:
        break
    # opt 转换为字节对象
    tcp_client_socket.send(opt.encode('utf-8'))
    data = tcp_client_socket.recv(BUF_SIZE)
    if not data:
        break
    # 将字节对象转换为字符串
    print(data.decode('utf-8'))
tcp_client_socket.close()
