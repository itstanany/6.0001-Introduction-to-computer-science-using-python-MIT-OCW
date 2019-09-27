# -*- coding: utf-8 -*-
'''
Created on Fri Sep 27 22:13:22 2019

@author: Ahmed Ali Mohamed

*******

Finger Exercise 
Chapter 7 section 2

*******

*******

Finger Exercise: Implement a function that satisfies the specification
def findAnEven(L):
"""Assumes L is a list of integers
Returns the first even number in L
Raises ValueError if L does not contain an even number"""


*******
'''
def findAnEven(L):
    """Assumes L is a list of integers
    Returns the first even number in L
    Raises ValueError if L does not contain an even number"""
    for e in L:
        if e%2 == 0:
            return e
        else:
            e = e
    raise ValueError('The provided list does not contain an even number')
    return None

