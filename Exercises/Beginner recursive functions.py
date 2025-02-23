# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 20:02:01 2022

@author: ander
"""
#factorials
def factorial (n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
#sum digits
def sum_digits(n):
    
    if n <10:
        return n
    else:
        all_but_last = n //10
        last = n%10
        return sum_digits(all_but_last)+last

#fibonacci

def fib (n):
    if n ==1:
        return 0
    elif n ==2:
        return 1
    else:
        return fib(n-1) +fib(n - 2)
    
# Palindrome
def isPalindrome (s):
    if len(s)<=1:
        return True
    else:
        return s[0]==s[-1] and isPalindrome(s[1:-1])
    
#Learning OOP
    
    
mylist=[]
count= 0
for count in range(3):
    while count < 3:
        count +=1
        mylist = eval(input('Enter value:'))
        break
    
'''
'''
mylist=[]

for i in range(6):
     num= eval(input('Enter value: '))
     mylist.append(num)
print(mylist)
# LIst and hwo to create them 
li=[]

num=0

while num >=0:
     num =eval(input('Enter value:'))
     li.append(num)
     
#Module 3.3 Q2 Print least non-negative

     value= 0 
     count= 0
     least= 0
     while value >=0:
         count+=1
         value= float(input('Enter number (negative to exit): '))
         if value <0 and count==1:
             print('No numbers')
             quit()
         elif value >=0: 
             least = value
     least = round(least,1)
     print('Least number is:', least)