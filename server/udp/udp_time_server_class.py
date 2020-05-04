#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/5/4 --

from socket import *
from time import ctime


class UdpServer:
    def __init__(self, host, port):
        self.udp_server = socket(AF_INET, SOCK_DGRAM)
        self.udp_server.bind((host, port))

    def send(self, data, addr):
        self.udp_server.sendto(('[%s] %s' % (ctime(), data.decode("utf-8"))).encode("utf-8"), addr)

    def recv(self, buf_size):
        return self.udp_server.recvfrom(buf_size)

    def close(self):
        self.udp_server.close()


def main():
    host = ''
    port = 23333
    buf_size = 1024

    udp_server = UdpServer(host, port)

    while True:
        print(" waiting for message ...")
        data, addr = udp_server.recv(buf_size)
        if not data:
            break
        udp_server.send(data, addr)
        print("... received from and returned to:", addr)


if __name__ == '__main__':
    main()
