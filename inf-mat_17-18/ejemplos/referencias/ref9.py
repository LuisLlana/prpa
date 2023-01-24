#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref9.py,v 1.1 2012-01-10 08:45:33 luis Exp $

def fun(l1,l2):
    l1[0]=l2
    l2[0]=1000
    l1[0][1]=2000

x=[0,1,2,3]
y=[6,7,8]
fun(x,y)
print("c1-x:{0}".format(x))
print("c1-y:{0}".format(y))
