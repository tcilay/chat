#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/5/4 --

import socket


class UdpClient:

    def __init__(self):
        self.udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, data, host, port):
        self.udp_client.sendto(data.encode("utf-8"), (host, port))

    def recv(self, buf_size):
        return self.udp_client.recvfrom(buf_size)


def main():
    host = '127.0.0.1'
    port = 23333
    buf_size = 1024

    udp_client = UdpClient()

    while True:
        opt = input(">")
        if not opt:
            break
        udp_client.send(opt, host, port)
        data, addr = udp_client.recv(buf_size)
        if not data:
            break
        print("[%s] %s" % (addr, data.decode("utf-8")))


if __name__ == '__main__':
    main()
