#!/usr/bin/env python
from beginner_tutorials.srv import *
import rospy


def handle_add_two_init(req):
    print("Returning [%s + %s = %s]" %(req.a,req.b,(req.a+req.b)))
    return AddTwoInitsResponse(seq.a+ req.b)