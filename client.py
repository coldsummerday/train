#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import PIL
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('192.168.43.17', 9999))
# 接收欢迎消息:


while True:
    data=raw_input("what you want to send\n")
    if data =='close':
        break
    if os.path.isfile(data):
        imagedata =  PIL.Image.open(data)
        imagedata.show()
        imagedata.save(data)
        rbfile = open(data,'rb')
        size = os.path.getsize(data)
        print("len:%s" %(size))
        s.send("p:%s" %(size))
        send_len=0
        while True:
            if size -send_len >1024:
                imagedata = rbfile.read(1024) 
                send_len+=1024
                s.send(imagedata)
                print("send 1024")
            else:
                imagedata =rbfile.read(size-send_len)
                s.send(imagedata)
                print("send"+str(len(imagedata)))
                break
            
        continue
    s.send(data)
s.close()
