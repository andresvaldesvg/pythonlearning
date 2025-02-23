# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 16:30:18 2022

@author: Andres Valdes
"""

#Q10 Multiplization table
print ('Multiplication table till 10\n')
a= int(input('Please enter the multiplication number: \n'))

print ('The table of ', a, 'is below: \n')

for i in range (0,10):
    

    print (a, 'x', i, "=", a*i)
