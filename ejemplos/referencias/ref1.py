#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref1.py,v 1.1 2012-01-10 08:45:33 luis Exp $

x = [0,1,2]
y = x
y[0] = 7
print( "c1-x:{0}".format(x))
print( "c1-y:{0}".format(y))

x.append(3)
y[0] = 8
print( "c2-x:{0}".format(x))
print( "c2-y:{0}".format(y))


x = x + [3]
y[0] = 9
print( "c2-x:{0}".format(x))
print( "c2-y:{0}".format(y))


x.append(3)
y[0] = 10
print( "c3-x:{0}".format(x))
print( "c3-y:{0}".format(y))
