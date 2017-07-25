#!/usr/bin/env python
#!-*-coding:utf-8 -*-
import socket
import rospy
import std_msgs
import threading
import os
import argparse
import os.path
import re
import sys
import tarfile
import imghdr
import numpy as np
from six.moves import urllib
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='3'



def rosinit():
    talker = rospy.Publisher("chatter",std_msgs.msg.Float32,queue_size=20)
    rospy.init_node('tcpclassfy',anonymous=True)
    return talker

def tcplink(sock,addr):
    global talker
    #rate =rospy.Rate(10)
    while True:
        data=sock.recv(1024)
        if data=='exit' or not data:
            break
        if data=='c':
            cdata=sock.recv(1024)
            if cdata =='up':
                talker.publish(float(1.2))
            elif cdata=='down':
                talker.publish(float(2.2))
            elif cdata=='left':
                talker.publish(float(3.2))
            elif cdata=='right':
                talker.publish(float(4.2))
            print(cdata)
        if data=='v':
            vdata=sock.recv(1024)
            if vdata == ("前进"):
                talker.publish(float(1.2))
            elif vdata == ("后退"):
                talker.publish(float(2.2))
            elif vdata ==("向左"):
                talker.publish(float(3.2))
            elif vdata ==("向右"):
                talker.publish(float(4.2))
            print(vdata)
        if data[0]=='p':
            size=data.split(':')[1]
            size = int(size)
            recvd_data = 0
            imagefile = open('/sd/%s.jpg' %(str(size)),'wb')
            while  recvd_data < size:
                if size -recvd_data >1024:
                    pdata = sock.recv(1024)
                    recvd_data+=len(pdata)
                else:
                    pdata = sock.recv(1024)
                    lengh = len(pdata)
                    recvd_data+=len(pdata)
                imagefile.write(pdata) 
            print("image recv over\n")
            imagefile.close()
            imgtype = imghdr.what('/sd/%s.jpg' %(str(size)))
            classcification,score = classfy('/sd/%s.jpg' %(str(size)))
            print(classcification,score)
            if score<0.02:
                continue
            
            talker.publish(swithClassfiCation(classcification))
	#else:
	    #talker.publish("Not find")
    sock.close()

def swithClassfiCation(classcification):
    if classcification=='clothes':
        return float(5.2)
    if classcification=='drink':
        return float(6.2)
    if classcification=='householdproducts':
        return float(7.2)
    if classcification=='snacks':
        return float(8.2)
    return(float(9.2))


def getLabels(labelsName):
    labels = []
    for label in tf.gfile.GFile(labelsName):
        labels.append(label.rstrip())
    return labels
def create_graph(gfile):
    with tf.gfile.FastGFile(gfile,'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def,name='')



def classfy(imagefile):
    global labels
    if not tf.gfile.Exists(imagefile):
        tf.logging.fatal("File does not exist %s" % imagefile)
    image_data = tf.gfile.FastGFile(imagefile,'rb').read()
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name("final_result:0")
        predictions = sess.run(softmax_tensor,{'DecodeJpeg/contents:0':image_data})
        top = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for index in top:
            human_string = labels[index]
            score = predictions[0][index]
            return human_string,score



def sockinit():
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('192.168.0.114',9999))
    s.listen(5)
    return s
    
if __name__=="__main__":
    labels=getLabels('/home/ubuntu/marketcar/marketcar.txt')
    create_graph('/home/ubuntu/marketcar/marketcar.gp')
    talker = rosinit()
    sock=sockinit()
    print("init finished") 
    while True:
        s,addr=sock.accept()
        print("connect")
        tcplink(s,addr)
        
