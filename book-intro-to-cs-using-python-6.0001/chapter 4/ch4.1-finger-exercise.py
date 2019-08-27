# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 17:32:07 2019

@author: Ahmed Ali
-------
Finger exercise Chapter 4 section 1
-------
*******
Finger exercise: Write a function isIn that accepts two strings as arguments and
returns True if either string occurs anywhere in the other, and False otherwise.
Hint: you might want to use the built-in str operation in.
*******
"""
#solution
first_string = input('Please, Enter a string: ')
second_string = input('Please, Enter a second string: ')
def isIn(x, y):
    if(str(x) in str(y)):
        return print('True')
    elif(str(y) in str(x)):
        return print(True)
    else:
        return print(False)
isIn(first_string, second_string)