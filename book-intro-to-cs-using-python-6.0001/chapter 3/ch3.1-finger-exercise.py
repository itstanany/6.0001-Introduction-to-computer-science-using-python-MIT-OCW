# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:35:41 2019

@author: Ahmed Ali
---
chapter 3 section 1
---
*******
Finger exercise: Write a program that asks the user to enter an integer and prints
two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.
*******
"""
ui = int(input('Pleaser Enter a Positive Integer: '))
if ui < 0:
    root = -20
else:    
    root = 0
pwr = 1
while root < 1000000:
    while pwr < 6:
        # we  add the second conditional to ensure that the integers less than 20 don't give rsult of the integer itself to power 1
        if ((root**pwr) == ui and root != ui and pwr != 6):
            break
        else:
            pwr = pwr + 1
    if ((root**pwr) == ui and root != ui and pwr != 6):
        break
    else:
        pwr = 1
        root = root + 1
if ((root**pwr) == ui and root != ui and pwr != 6):
    print(' The root of', ui, 'is', root, 'to power', pwr)
else:
    print('No root found for the entered integer in the intervals root = [-20, 20] and power = [1, 5]')
