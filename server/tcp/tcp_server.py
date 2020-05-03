#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/5/3 --

"""
    TCP服务器伪代码
    ss = socket()                   # 创建伪代码
    ss.bind()                       # 套接字与地址绑定
    ss.listen()                     # 监听连接
    inf_loop:                       # 服务器无线循环
        cs = ss.accept()            #接受客户端连接
        comm_loop:                  #通信循环
            cs.recv()/cs.send()     # 对话（接受/发送）
        cs.close()                  # 关闭客户都套接字
    ss.close()                      # 关闭服务器套接字 #（可选）

"""
from socket import *
from time import ctime

HOST = ''
PORT = 23333
BUF_SIZE = 1024
ADDR = (HOST, PORT)

tcp_server_socket = socket(AF_INET, SOCK_STREAM)
tcp_server_socket.bind(ADDR)
tcp_server_socket.listen(5)

while True:
    print("waiting for connection ...")
    tcp_client_socket, addr = tcp_server_socket.accept()
    print("... connected from: ", addr)

    while True:
        # tcp_client_socket.recv(BUF_SIZE) 返回字节对象
        # decode("utf-8") 按utf-8解码,汉字可以显示
        data = tcp_client_socket.recv(BUF_SIZE).decode("utf-8")
        if not data:
            break
        tcp_client_socket.send(('[%s] %s' % (bytes(ctime(), 'utf-8'), data)).encode('utf-8'))
        # a bytes-like object is required, not 'str'
        # send() 需要一个字节对象，需要使用encode()函数编码为字节对象
    tcp_client_socket.close()
tcp_server_socket.close()
