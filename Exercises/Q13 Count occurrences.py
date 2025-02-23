# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 19:08:01 2022

@author: Andres Valdes
"""

string = str(input("enter string: "))

word = str(input('Enter word: '))

result = [i for i in range (len(string))
          if string.startswith(word,i)]

print('The count of the word is: ', len(result))
