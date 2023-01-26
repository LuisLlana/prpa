#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref2.py,v 1.1 2012-01-10 08:45:33 luis Exp $

def fun1(a):
    a[0] = 7

def fun2(a):
    a = 7

x = [0,1,2]
y = 0
fun1(x)
fun2(y)
print("c1-x:{0}".format( x))
print("c1-y:{0}".format(y))
