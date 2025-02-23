# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 20:12:43 2022

@author: Andres Valdes
"""

#Q6 Time conversion

print ('Time converter from seconds. \n')


seconds = eval(input ('Please enter the seconds up to (86400 s) to be converted: \n'))

hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %=60
seconds2 = seconds



print('Hours: ', hours)
print('Minutes: ', minutes)
print('Seconds: ', seconds2)

print('Time: ', hours, minutes, seconds )
