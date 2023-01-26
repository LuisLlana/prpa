#!/usr/bin/python
# -*- coding: utf-8 -*-
# $Id: ref4.py,v 1.1 2012-01-10 08:45:33 luis Exp $

x = "Hola"
y = x
x.replace("H","X")
print("c1-x:{0}".format(x))
print("c1-y:{0}".format(y))

x = x.replace("H","X")

print("c2-x:{0}".format(x))
print("c2-y:{0}".format(y))
