#!/usr/bin/python
# coding: utf-8

def is_prime(num):
    '''
    This function checks if num is prime

    Parameters
    ----------
    num : integer
    Integer number to study.

    Returns
    -------
    boolean
    True if num is prime, False otherwise

    Example
    -------
    >>> is_prime(6)
    False
    >>> is_prime(7)
    True

    '''
    i = 2
    while i*i <= num and num%i != 0:
        i += 1
    return i*i > num

def next_prime(num):
    '''
    Find the smaller prime >= num

    Parameters
    ----------
    num : integer
    Integer number to study.

    Returns
    -------
    int
    Smaller prime >= n

    Example
    -------
    >>> next_prime(6)
    7
    '''
    while not is_prime(num):
        num = num + 1
    return num



def main():
    n = 100
    i = 1
    prime = 2 # 2 is the first prime number
    while i < n:
        print i, prime
        prime = next_prime(prime+1)
        i = i + 1
