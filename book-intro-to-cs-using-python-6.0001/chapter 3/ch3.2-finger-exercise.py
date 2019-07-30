# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:42:12 2019

@author: Ahmed A T
--- 
chapter 3 section 2
---
*******
Finger exercise: Let s be a string that contains a sequence of decimal numbers
separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the
sum of the numbers in s.
*******
"""

s = '1.23,2.4,3.123'
list1 = s.split(',')
list2 = []
for i in list1:
    list2.append(float(i))
total2 = 0
for a in list2:
    total2 = total2+ a
    
print(total2)

