#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref3.py,v 1.1 2012-01-10 08:45:33 luis Exp $

x = "Hola"
y = x
print("c0:{0}".format( y[0]))
y[0] = 'X'
print("c1-y:{0}".format( y))
print("c1-x:{0}".format( x))
