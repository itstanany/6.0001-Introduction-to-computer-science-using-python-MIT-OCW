# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 13:53:45 2019

@author: Ahmed Ali
*******
problem set one
part B
 the problem set description from the file:
Part C: Finding the right amount to save away
    In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
and your annual raise affect how long it takes you to save for a down payment.  This is nice, but
suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
How much should you save each month to achieve this?  In this problem, you are going to write a 
program to answer that question.  To simplify things, assume:
    1. Your semi­annual raise is .07 (7%)
    2. Your investments have an annual return of 0.04 (4%)  
    3. The down payment is 0.25 (25%) of the cost of the house 
    4. The cost of the house that you are saving for is $1M.
    You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
the required down payment. 
    In ps1c.py, write a program to calculate the best savings rate, as a function of your starting salary.
You should use bisection search to help you do this efficiently. You should keep track of the number of 
steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote
for part B in this problem.  
    Because we are searching for a value that is in principle a float, we are going to limit ourselves to two
decimals of accuracy (i.e., we may want to save at 7.04% ­­ or 0.0704 in decimal – but we are not 
going to worry about the difference between 7.041% and 7.039%).  This means we can search for an
integer between 0 and 10000 (using integer division), and then convert it to a decimal percentage
(using float division) to use when we are calculating the current_savings after 36 months. By using
this range, there are only a finite number of numbers that we are searching over, as opposed to the
infinite number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we
use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code
should print out a decimal (e.g. 0.0704 for 7.04%).
    Try different inputs for your starting salary, and see how the percentage you need to save changes to
reach your desired down payment.  Also keep in mind it may not be possible for to save a down
payment in a year and a half for some salaries. In this case your function should notify the user that it 
is not possible to save for the down payment in 36 months with a print statement. Please make your
program print results in the format shown in the test cases below.   
    Note: There are multiple right ways to implement bisection search/number of steps so your
results may not perfectly match those of the test case. 
Hints
    ● There may be multiple savings rates that yield a savings amount that is within $100 of the
    required down payment on a $1M house. In this case, you can just return any of the possible
    values.
    ● Depending on your stopping condition and how you compute a trial value for bisection search,
    your number of steps may vary slightly from the example test cases.
    ● Watch out for integer division when calculating if a percentage saved is appropriate and when
    calculating final decimal percentage savings rate.
    ● Remember to reset the appropriate variable(s) to their initial values for each iteration of bisection
    search.
"""
# THE SOLUTION TO PART C OF PROBLEM SET ONE
#initial annual salary to save the starting value
initial_a_s = float(input('Please, Enter Starting Salary: '))
#annual Salary
a_s = initial_a_s
total_cost = 1000000.0 
#annual return
r = 0.04
#semi annual raise
s_a_r = 0.07 # nest time get it from the user
#portion down payment
portion_d_p = 250000.0 #total_cost * 0.25
low = 0.0
high = 1.0
#guess
g = (low + high ) / 2
#monthly_salary saved
m_s_s = (initial_a_s / 12) * g
#current savings
current_sv = 0.0
#months
m = 0
#Number Of Guesses
NoOfGs = 0
if ((3 * initial_a_s )+ (initial_a_s* r)) <= portion_d_p:
    print('It is not possible to pay the down payment in three years.')
else:
    while abs(current_sv - portion_d_p) > 100:
        current_sv = 0.0
        while m < 36:
            if ((m - 1)%6 == 0) and (m != 1):
                a_s = a_s + (a_s * s_a_r)
                m_s_s = (a_s/12) * g
            current_sv = current_sv + (current_sv * (r/12)) + m_s_s
            m = m + 1
        NoOfGs = NoOfGs + 1
        a_s = initial_a_s
        m = 0
        if abs(current_sv - portion_d_p) > 100:
            if current_sv > portion_d_p:
                high = g
            else:
                low = g
            g = (high + low) /2
            m_s_s = (initial_a_s / 12) * g
        else:
            print('Best savings rate:', round(g, 4))
            print('Steps in bisection search:', NoOfGs)
            break
