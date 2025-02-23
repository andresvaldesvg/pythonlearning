# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 19:10:03 2022

@author: Andres Valdes
"""
age = eval(input("Enter age: "))
gender = str(input('Enter gender (M/F): '))
day = eval(input('Enter days: '))

wm = 750
wf = 850
wm1 = 900
wf1 = 950


if gender =="M":
    gender = 1
    if age >= 18 and age <35:
        print("Total wages: ", wm * day)
    elif age >=35 and age <=40:
        print('Total wages: ', wm1 * day)
    else:
        print('Invalid input')
             
else:
    gender = 0
    if age >= 18 and age <35:
        print("Total wages: ", wf * day)
    elif age >=35 and age <=40:
        print('Total wages: ', wf1 * day)
    else:
        print('Invalid input')