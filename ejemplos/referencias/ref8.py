#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref8.py,v 1.1 2012-01-10 08:45:33 luis Exp $


def fun(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a

x=12
y=18
z=fun(x,y)
print("c1-x:{0}".format( x))
print("c1-y:{0}".format( y))
print("c1-z:{0}".format( z))

x=3000
y=7
z=fun(x,y)
print("c2-x:{0}".format( x))
print("c2-y:{0}".format( y))
print("c2-z:{0}".format( z))
