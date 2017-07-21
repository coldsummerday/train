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

import numpy as np
from six.moves import urllib
import tensorflow as tf



def tcplink(sock,addr):
    global talker
    while True:
        data=sock.recv(1024)
        if data=='exit' or not data:
            break
        print(data)
        if os.path.isfile(data):
            classification=classfy(data)
            talker.publish(classification)
        else:
            print('error to classify %s' %(data))
        '''
        if data=='c':
            cdata=sock.recv(1024)
            if cdata =='up':
                talker.publish('up')
            elif cdata=='down':
                talker.publish('down')
            elif cdata=='left':
                talker.publish('left')
            elif cdata=='right':
                talker.publish('right')
            print(cdata)
        if data=='v':
            vdata=sock.recv(1024)
            if vdata == ("向上"):
                talker.publish('up')
            elif vdata == ("向下"):
                talker.publish('down')
            elif vdata ==("向左"):
                talker.publish('left')
            elif vdata ==("向右"):
                talker.publish('right')
            print(vdata)
        if data=='p':
            break
        if os.path.isfile(data):
            #classification=classfy(data)
            #talker.publish(classification)
        '''
	#else:
	    #talker.publish("Not find")
    sock.close()

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
            return human_string



def sockinit():
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('192.168.0.114',9999))
    s.listen(1)
    return s
def getTalker():
    talker=rospy.Publisher('controller',std_msgs.msg.String,queue_size=20)
    rospy.init_node("tcpclassfy",anonymous=True)
    return talker
    
if __name__=="__main__":
    talker=getTalker()
    labels=getLabels('/home/ubuntu/marketcar/marketcar.txt')
    create_graph('/home/ubuntu/marketcar/marketcar.gp')
    sock=sockinit()
    while True:
        s,addr=sock.accept()
        tcplink(s,addr)
