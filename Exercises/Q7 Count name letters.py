# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 21:39:21 2022

@author: Andres Valdes
"""

name = input('Enter name: ')
count = 0
for a in name:
    if(a.isalpha())== True:
       count +=1
print ('Your full name is', name,'and it has', count, 'characters' )