# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:01:16 2022

@author: ander
"""

print('Enter subject note: \n')



s1= int(input('subject note'))
s2= int(input('subject note'))
s3= int(input('subject note'))
s4= int(input('subject note'))
s5= int(input('subject note'))

a= (s1+s2+s3+s4+s5)/5

if s1>0 and s1<100:
    print(s1)
elif s2>0 and s2<100:
    print(s2)
elif s3>0 and s3<100:   
    print(s2)
elif s4>0 and s4<100:
    print(s2)
elif s5>0 and s5<100:
   print(s2)

 
print ('Average: ', a)