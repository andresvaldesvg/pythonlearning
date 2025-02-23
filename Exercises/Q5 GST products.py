# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 20:36:34 2022

@author: Andres 
"""

#Q5 group activity

print ('Groseries calculator. Please enter the cuantity of elements: \n')

milk1 = eval  (input('Milk: \n'))
bread1 = eval (input('Bread: \n'))
egg1 = eval (input('Eggs: \n'))

milk = 2
bread = 3
egg = 0.50

gst = (10/100)* milk
gst1 = (10/100)* bread

value = (milk1 + gst)*milk1
value1 = (bread1 + gst1)*bread1
value2 = egg * egg1

print ('Dear customer, the value for your purchase has shown below: \n')
print ('Milk with GST: ', value, '$')
print ('Bread with GST: ', value1, '$')
print ('Eggs: ', value2, '$\n')
print ('Total: ', int(value+value1+value2),'$')

print('Thanks for supporting our business!!!!')