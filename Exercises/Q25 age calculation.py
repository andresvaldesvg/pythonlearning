# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 22:40:01 2022

@author: Andres Valdes
"""

    
from datetime import date
 
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def age_coll ():
    y = int(input('Year'))
    d = int(input('Day'))
    m = int(input('Month'))
    agefinal = age(date(y, d, m)) 
    return  agefinal


def age_check():
    if age_coll() >= 16:
        print('Pass')
    else:
        print('Denied')
age_check()