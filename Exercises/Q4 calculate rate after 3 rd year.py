# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:19:11 2022

@author: ander
"""
#Q4 Challenge, calculate the rate after 3 years


print ('Calculate your interest rate for the next 3 years \n')
name = input('Please enter your name: \n')
number = input('Enter your contact number: \n')
rate = input ('Enter your interest rate: \n')
amount = input ('How much would you deposit: \n')


print('Hi ', name,' you have deposited = ', amount) 
print ('Your interest rate is: ', rate,'%')

rate = int (rate) 
amount = int (amount)

result = (rate /100) * amount

x = result + amount

print ('Amount after 1st year: ', x)

result2 = (rate /100) * x

z = x + result2

print ('Amount after 2nd year: ', z)

result3 = (rate /100) * z

q = z + result3

print ('Amount after 3rd year: ', q)