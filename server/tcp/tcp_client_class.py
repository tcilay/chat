#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/5/4 --

from socket import *


class TcpClient:
    def __init__(self, *addr):
        self.tcp_client = socket(AF_INET, SOCK_STREAM)
        self.tcp_client.connect(*addr)

    def __init__(self, host, port):
        self.tcp_client = socket(AF_INET, SOCK_STREAM)
        self.tcp_client.connect((host, port))

    def send(self, data):
        self.tcp_client.send(data.encode("utf-8"))

    def recv(self, buf_size):
        recv_data = self.tcp_client.recv(buf_size)
        return recv_data.decode("utf-8")

    def close(self):
        self.tcp_client.close()


def main():
    host = "127.0.0.1"
    port = 23333
    buf_size = 1024

    tcp_client = TcpClient(host, port)
    while True:
        opt = input(">")
        if not opt:
            break
        tcp_client.send(opt)
        recv_data = tcp_client.recv(buf_size)
        if not recv_data:
            break
        print(recv_data)
    tcp_client.close()


if __name__ == '__main__':
    main()
