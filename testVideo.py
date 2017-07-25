#!/usr/bin/env python
#!-*-coding:utf-8 -*-

import cv2
def initCam():
    try:
        cap = cv2.VideoCapture(1)
    except:
        cap = cv2.VideoCapture(0)
    return cap

def shotToSave(fileName):
    global cap
    ret,frame = cap.read()
    cv2.imwrite(fileName,frame)


if __name__=="__main__":
    cap = initCam()
    

    shotToSave("2.jpg")
