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
        
# if two numbers only are odd.
elif x%2 != 0 and y%2 != 0:
    if x < y:
        print("The Largest Odd Number is Y =", y)
    else:
        print("The Largest Odd Number is X =", x)
elif x%2 != 0 and z%2 != 0:
    if z > x:
        print("The Largest Odd Number is Z =", z)
    else:
        print("The Largest Odd Number is X =", x)
        
elif y%2 != 0 and z%2 != 0:
    if z > y:
        print("The Largest Odd Number is Z =", z)
    else:
        print("The Largest Odd Number is Y =", y)

# only one user input is odd
elif x%2 != 0:
    print("The Only and Largest Odd Number is X =", x)
elif y%2 != 0:
    print("The Only and Largest Odd Number is Y =", y)
elif z%2 != 0:
    print("The Only and Largest Odd Number is Z =", z)
    
# No Odd Numbers entered    
else:
    print('Please Enter Odd Numbers!')