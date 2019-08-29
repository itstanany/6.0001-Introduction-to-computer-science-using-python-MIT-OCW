# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:06:21 2019

@author: Ahmed Ali Mohamed
-------
Chapter 4 section 3.1   (4.3.1)
-------

*******
Finger exercise: When the implementation of fib in Figure 4.7 is used to compute
fib(5), how many times does it compute the value of fib(2) on the way to computing fib(5)?
*******
"""

'''
The solution is '3' three times
'''

# code to track how many times the specific has been called
number_to_fib = int(input('Please, Enter a positive integer: '))
# the umber user want to track how many it is called during getting Fibonacci of the input
specific_number_to_be_counted = int(input('Please, Enter a positive integer to track how many it is called? '))
def fib(n):
    '''
    Assumes, n int >= 0
    return fibbonachi of n
    '''
    global numFibCalls
    numFibCalls = 0
    numFibCalls += 1
    global numFibTwo
    if n == specific_number_to_be_counted:
        numFibTwo += 1
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(x):
    global numFibCalls
    numFibCalls = 0
    global numFibTwo
    numFibTwo = 0
    print('the Fibbonaci number of:', x, 'is', fib(x))
    print('Fib function has been called', numFibCalls, 'times')
    print('Fib(',specific_number_to_be_counted,') function has been called', numFibTwo, 'times')
    return None
testFib(number_to_fib)
