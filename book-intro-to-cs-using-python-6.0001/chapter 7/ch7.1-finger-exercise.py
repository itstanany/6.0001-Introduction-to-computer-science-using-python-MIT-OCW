# -*- coding: utf-8 -*-
'''
Created on Fri Sep 27 20:05:54 2019

@author: Ahmed Ali Mohamed
*******

Finger exercise chapter 7 section 1

*******



*******

Finger exercise: Implement a function that meets the specification below. Use a
try-except block.
def sumDigits(s):
"""Assumes s is a string
Returns the sum of the decimal digits in s
For example, if s is 'a2b3c' it returns 5"""

*******

'''

# the solution

# string containing all decimal digits
digits = '0123456789'
def sumDigits(s):
    '''
    Assumes s is a string
    Returns the sum of the decimal digits in s
    For example, if s is 'a2b3c' it returns 5
    '''
    # variable to save the sum of decimal digits
    sum = 0
    #loop through each index of the string argument s
    for e in s:
        # try to adding the ndex value to the sum
        try:
            # casting "e" variable from string to integer number
            e = int(e)
            # if it's integer and raises no exceptions, adding the value to the previous value
            sum = sum + e
        # if the "e" value isn't decimal, return the sum with no operations
        except ValueError:
            sum = sum
    # finally, return the sum value 
    return sum

