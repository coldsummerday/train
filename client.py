#!/usr/bin/env python
# -*- coding: utf-8 -*-



import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.199.154', 9999))
# 接收欢迎消息:


while True:
    data=raw_input("what you want to send\n")
    if data !='close':
        break
    s.send(data)
s.close()