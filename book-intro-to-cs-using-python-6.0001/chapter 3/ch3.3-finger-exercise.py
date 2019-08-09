# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 21:36:08 2019

@author: Ahmed Ali
--------
chapter 3 section 3
--------
********
Finger exercise: What would have to be changed to make the code in Figure 3.4
work for finding an approximation to the cube root of both negative and positive
numbers? (Hint: think about changing low to ensure that the answer lies within
the region being searched.)
********
"""
# the solution
real_input = float(input('uuuuuPlease, Enter a perfect square: '))
u = abs(real_input) # u = absolute input
low = 0.0
high = max(1.0, u)
uNumberOfGuesses = 0
uepsilon = 0.01
uans = (high + low)/2
while abs(uans**3 - u) >= uepsilon:
    uNumberOfGuesses += 1
    if uans**3 < u:
        low = uans
    else:
        high = uans
    uans = (high + low)/2
print('uuuuuuuNumberOfGuesses:', uNumberOfGuesses)
if real_input < 0:
    uans= -uans
if abs(abs(uans**3) - u) >= uepsilon:
    print('Can\'t find cube root of:', u)
else:
    print(uans, 'is close to square root of:', u)
    

