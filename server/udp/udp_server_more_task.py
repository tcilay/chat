#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/25 --
# !/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay --
# -- date:2020/4/25 --
import socket
from threading import Thread


def send_msg(upd_socket, ip, port):
    # ip = input("请输入ip:")
    # port = input("请输入端口号:")
    # 目标地址
    addr = (ip, int(port))
    while True:
        msg = input("请输入发送的信息：")
        # 发送数据
        if msg == "exit":
            break
        upd_socket.sendto(msg.encode("GBK"), addr)


def rev_msg(udp_socket):
    while True:
        # 接收数据
        msg = udp_socket.recvfrom(1024)
        # (msg[1], msg[0].decode("GBK")) : (地址,解码数据)
        print("\n%s:%s" % (msg[1], msg[0].decode("GBK")))


def main():
    # 创建套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    upd_socket.bind(("", 2333))
    ip = input("请输入ip:")
    port = input("请输入端口号:")
    # while True:
    send = Thread(target=send_msg, args=(upd_socket, ip, port))
    send.start()

    rev = Thread(target=rev_msg, args=(upd_socket,))
    rev.start()

    # # 关闭
    # upd_socket.close()


if __name__ == '__main__':
    main()
