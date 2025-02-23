# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 22:28:24 2022
@author: Name: Andres David Valdes Gonzalez
ID: A00062146
"""
#Module 4 Q2 Celcius to Fahrenheit 
#value asked
value = float(input('Enter value to be converted: '))
# Creation of 2 functions to convert
def conver_Celsius(fah):
    c= fah *9/5 + 32
    return c


def conver_Fahrenheit(cel):
    f = (cel - 32) *5/9
    return f
#Extra function to carry the numbers

def show_values():
    result = conver_Celsius(value)
    result2 = conver_Fahrenheit(value)
    return result, round(result2,2)
show_values()

#Print value using the previous functions
print('This is the result for Celsius, Fahrenheit: ', show_values())