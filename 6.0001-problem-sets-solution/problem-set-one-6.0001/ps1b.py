# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:43:30 2019

@author: Ahmed Ali
*******
problem set one
part B
 the problem set description from the file:
     Part B: Saving, with a raise
     Background 
         In Part A, we unrealistically assumed that your salary didn’t change.  But you are an MIT graduate, and
     clearly you are going to be worth more to your company over time! So we are going to build on your
    solution to Part A by factoring in a raise every six months. 
    In ps1b.py, copy your solution to Part A (as we are going to reuse much of that machinery).  Modify
    your program to include the following
        1. Have the user input a semi-annual salary raise semi_annual_raise (as a decimal percentage)
        2. After the 6th month, increase your salary by that percentage.  Do the same after the 12th
            month, the 18th month, and so on. 
Write a program to calculate how many months it will take you save up enough money for a down
payment.  LIke before, assume that your investments earn a return of r = 0.04 (or 4%) and the
required down payment percentage is 0.25 (or 25%).  Have the user enter the following variables:
    1. The starting annual salary (annual_salary)
    2. The percentage of salary to be saved (portion_saved)
    3. The cost of your dream home (total_cost)
    4. The semi­annual salary raise (semi_annual_raise)
Hints
To help you get started, here is a rough outline of the stages you should probably follow in writing your
code:
    ● Retrieve user input. 
    ● Initialize some state variables. You should decide what information you need.  Be sure to be
    careful about values that represent annual amounts and those that represent monthly amounts.
    ● Be careful about when you increase your salary – this should only happen after the 6th, 12th, 18th
      month, and so on. 
Try different inputs and see how quickly or slowly you can save enough for a down payment.  Please
make your program print results in the format shown in the test cases below.   

*******
"""

