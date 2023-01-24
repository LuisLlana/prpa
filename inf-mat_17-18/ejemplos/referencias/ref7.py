#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref7.py,v 1.1 2012-01-10 08:45:33 luis Exp $

def fun(l1,l2):
    l2[1] = 100*l2[1]
    l2 = l1
    l2.extend([4,5])

x = [0,1,2,3]
y = [7,8,9,10]
fun(x,y)
print( "c1-x:{0}".format(x))
print( "c1-y:{0}".format(y))

fun(x,x)
print( "c2-x:{0}".format(x))

fun(x,x+[20])
print( "c3-x:{0}".format(x))

fun(x+[30],x)
print( "c4-x:{0}".format(x))

fun(x.append(40),x)
print( "c5-x:{0}".format(x))
