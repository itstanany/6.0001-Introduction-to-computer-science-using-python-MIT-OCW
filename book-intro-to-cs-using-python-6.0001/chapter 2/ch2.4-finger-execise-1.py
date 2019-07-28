# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:19:12 2019

@author: Ahmed Ali
--- chapter 4 section 4 ---
Finger Exercise 1

*******
Finger exercise: Replace the comment in the following code with a while loop.
numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
#concatenate X to toPrint numXs times
print(toPrint)
*******
"""

numXs = int(input('How many times should I print the letter X? '))
toPrint = ''
i = 1
while(i <= numXs):
    toPrint += 'X'
    i += 1
print(toPrint)

