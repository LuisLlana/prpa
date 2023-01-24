# -*- coding: utf-8 -*-
"""
Soluciones al examen parcial de Febrero
Curso 2016/2017
Created on Sat Jan 28 19:19:12 2017
"""

def gcd(a, b):
    '''
    Given two integers a and b, calculate
    the greater common divisor of these numbers.
    We consider the following algorithm:
    * gcd(a, b) = gcd (b, a)
    * if a >= b, gcd(a, b) = gcd(a-b, b)
    * gcd(a, 0) = a
    Assume a, b positive integers
    Parameters:
    ------------
    a, b : int
        two positive integers

    Returns
    -------
    int
       the greates common divisor

    Example
    -------
    >>> gcd(3, 4)
    1
    >>> gcd(12, 8)
    4

    '''
    while b != 0:
        if a < b:
            a, b = b, a
        a = a - b
    return a


def communitary(lst):
    '''
    We determine if the list of integers lst is communitary. That is,
    there existe a common divisor d > 1 for all the integers
    of the list.

    Parameters:
    ------------
    lst : [int]
        list of integers

    Returns
    -------
    bool
       if the list is communitary or not

    Example
    -------
    >>> communitary([2,4,6,8])
    True
    >>> communitary([2,4,6,3])
    False

    '''
    result = True
    if len(lst) > 1:
        div = gcd(abs(lst[0]), abs(lst[1]))
        i = 2
        while i < len(lst) and div != 1:
            div = gcd(div, abs(lst[i]))
            i = i + 1
        result = (div != 1)
    elif len(lst) == 1:
        result = abs(lst[0]) != 1
    else:
        result = False
    return result

def reverse_num(number):
    '''
    We calculate the reverse of an integer number. The result is
    another integer number.

    Parameters:
    ------------
    number : int
        integer

    Returns
    -------
    int
       the reverse of num

    Example
    -------
    >>> reverse(1234)
    4321
    >>> reverse(12000)
    21

    '''
    reverse = 0
    while number != 0:
        reverse = 10* reverse + (number % 10)
        number = number / 10
    return reverse

def do(a):
    print a
    b = a + 1
    do1(b)
    do2(b)
    
def do1(b):
    print b
    c = b + 2
    do2(c)
    
def do2(c):
    print c*c  



def check(a, b, c):
  return (b % 3 < 2) and (a[6] > c[0])
  
def grade(mark):
  msg = 'Suspenso'

  if mark >= 5 and mark < 7:
    msg = 'Aprobado'
  elif mark < 9:
    msg = 'Notable'
  else:
    msg = 'Sobresaliente'
    
  return msg

from PIL import Image

def create_image():
  img = Image.new("L", (50, 100), 0)
  
  for i in range(100):
    for j in range(50):
        if (i - 25)**2 + (j - 50)**2 <=20**2:
            img.putpixel((i, j), 255)
    
  return img

def do1(a):
    b = a // 2
    c = b // 2
    do2(b,a)
    do3(a,b,c)

def do2(a,b):
    d = b * 2.0
    do3(a,b,d)
    
def do3(a,b,c):
    if a >= b and b >= c:
        print a-(b+c)
    else:
        print c-(a+b)
        


def main():
    '''
    Test function
    '''
    lst1 = range(2, 20, 2)
    print lst1, communitary(lst1)
    lst2 = lst1 + [3]
    print lst2, communitary(lst2)
    lst3 = [5] + lst2
    print lst3, communitary(lst3)


