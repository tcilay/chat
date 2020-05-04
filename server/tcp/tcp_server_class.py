#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/5/4 --

from socket import *
from time import ctime


class TcpServer:

    def __init__(self, host, port):
        self.tcp_server = socket(AF_INET, SOCK_STREAM)
        self.tcp_server.bind((host, port))
        self.tcp_server.listen(5)

    def accept(self):
        """
            等待传入连接，返回一个新的套接字
            表示连接以及客户端的地址
            地址信息是元组表示（host,port）
        :return:
        """
        return self.tcp_server.accept()

    def send(self, data):
        self.tcp_server.send(data.encode("utf-8"))

    def recv(self, buf_size):
        data = self.tcp_server.recv(buf_size)
        return data.decode("utf-8")

    def close(self):
        self.close()


def main():
    host = ''
    port = 23333
    buf_size = 1024

    tcp_server = TcpServer(host, port)
    while True:
        cli_socket, addr = tcp_server.accept()
        data = cli_socket.recv(buf_size).decode("utf-8")
        if not data:
            break
        print(cli_socket)
        print("client send msg : %s ,addr is %s" % (data, addr))
        cli_socket.send(('[%s] %s' % (bytes(ctime(), 'utf-8'), data)).encode('utf-8'))
        cli_socket.close()
    tcp_server.close()


if __name__ == '__main__':
    main()
