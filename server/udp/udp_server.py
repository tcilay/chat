#!/usr/bin/env python
# -- coding:utf-8 --
# -- author:tcilay -- 
# -- date:2020/4/25 --
import socket


def send_msg(upd_socket):
    ip = input("请输入ip:")
    port = input("请输入端口号:")
    # 目标地址
    addr = (ip, int(port))
    while True:
        msg = input("请输入发送的信息：")
        # 发送数据
        if msg == "exit":
            break
        upd_socket.sendto(msg.encode("GBK"), addr)


def rev_msg(udp_socket):
    # 接收数据
    msg = udp_socket.recvfrom(1024)
    # (msg[1], msg[0].decode("GBK")) : (地址,解码数据)
    print("%s:%s" % (msg[1], msg[0].decode("GBK")))


def main():
    # 创建套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    upd_socket.bind(("", 2333))
    while True:
        print("----1.发送数据------")
        print("----2.接收数据------")
        print("----other.退出------")
        # send_msg(upd_socket)
        opt = input("请输入需要的操作")
        if "1" == opt:
            send_msg(upd_socket)
        elif "2" == opt:
            rev_msg(upd_socket)
        elif "exit" == opt:
            print("退出成功...")
            break
        else:
            print("输入有误,请重新输入...")
    # 关闭
    upd_socket.close()


if __name__ == '__main__':
    main()
