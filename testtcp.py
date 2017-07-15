#!/usr/bin/env python
# -*- coding: utf-8 -*-

'a server example which send hello to client.'

import time, socket, threading

def tcplink(sock, addr):
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        print(data)
    sock.close()
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('192.168.199.154', 9999))
s.listen(5)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()