# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 22:16:26 2022

@author: ander
"""
evenlist=[]
oddlist=[]
a = []
s = int(input("Enter the size of array: "))
for i in range(0, s):
    ele = int(input("Enter the elements of the array: "))
    a.append(ele)

if i in a:
    if (i %2==0):
        a = 0
        evenlist.append(i)
    else:
        a = 1
        oddlist.append(i)
    
print('even', evenlist)
print('odd', oddlist)
    
#    if num %2==0 in range (1):
        
 #    print('Maximum value even:', num)
     
 #   elif num %2==0 in range (2):
 #    print('Maximum value even:', num) 
   # elif num %2==0 in range (3):
   #   print('Maximum value even:', num) 
 #   elif num %2==0 in range (4):
  #    print('Maximum value even:', num) 
  #  elif num %2==0 in range (5):
    #  print('Maximum value even:', num) 
   # else: 
    #    print  ("No even found", max(num))          
                