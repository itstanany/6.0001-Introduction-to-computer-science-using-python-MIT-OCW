# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 21:58:17 2019

@author: Ahmed A T
--- chapter 2 section 4 ---
--- finger esercise 2 ---
*******
Finger exercise: Write a program that asks the user to input 10 integers, and then
prints the largest odd number that was entered. If no odd number was entered, it
should print a message to that effect.
*******
"""
a = int(input('Please enter an integer: '))
b = int(input('Please enter an integer: '))
c = int(input('Please enter an integer: '))
d = int(input('Please enter an integer: '))
e = int(input('Please enter an integer: '))
f = int(input('Please enter an integer: '))
g = int(input('Please enter an integer: '))
h = int(input('Please enter an integer: '))
i = int(input('Please enter an integer: '))
j = int(input('Please enter an integer: '))
if(a%2 == 0):
    a = 0
else:
    a = a
if(b%2 == 0):
    b = 0
else:
    b = b
if(c%2 == 0):
    c = 0
else:
    c = c
if(d%2 == 0):
    d = 0
else:
    d = d
if(e%2 == 0):
    e = 0
else:
    e =e
if(f%2 == 0):
    f = 0
else:
    f = f
if(g%2 == 0):
    g = 0
else:
    g = g
if(h%2 == 0):
    h = 0
else:
    h = h
if(i%2 == 0):
    i = 0
else:
    i = i
if(j%2 == 0):
    j = 0
else:
    j = j

values = a, b, c, d, e,f ,g, h, i, j

maximum = max(values)
if(maximum == 0):
    print('No odd Integers. Please, Enter at least one odd integer')
else:
    print(maximum, 'Is The Largest Odd Integer Added')