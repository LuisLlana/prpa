import math



def who_am_i_1(a, b, c):
    disc = b*b - 4*a*c
    if disc<0:
        raise Exception('Invalid equation')
    return 0.5 * (-b + math.sqrt(disc)), 0.5 * (-b - math.sqrt(disc))


def who_am_i_2(n):
    phi = 0.5 * (1 +math.sqrt(5))
    return int(0.5 + phi**n / math.sqrt(5))


def who_am_i_3(a, b):
    while a != 0:
        r = b % a 
        b = a
        a = r
    return b


def who_am_i_4(a, b):
    m = 0
    while a != 0:
        if a%2 != 0:
            m = m + b
        b = 2 * b
        a = a // 2 
    return m
    

                


