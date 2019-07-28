# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 16:14:02 2019

@author: Tanany
"""

# print the latgest odd input
print('Enter Three Numbers to Print the Largest Odd Number Entered')
x = float(int(input('Please enter a Number X ')))
y = float(int(input('Please enter a Number Y ')))
z = float(int(input('Please enter a Number Z ')))

# first check wheter the three are odd
if x%2 != 0 and y%2 != 0 and z%2 != 0:
    if x < y and y < z:
        print("The Largest Odd Number is Z =", z)
    elif z < x:
        print("The Largest Odd Number is X =", x)
    elif z < y:
        print("The Largest Odd Number is Y =", y)