# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 23:11:34 2022

@author: Andres Valdes
"""

class Person:
    def __init__(self, name, yearob = 0, gender = 'NA'):
        self.name = name
        self.yearob = yearob
        self.gender = gender
    def age_calculation(self):
        currentyear = 2022
        self.yearob -= currentyear
        print('Age is', abs(self.yearob))
    def display(self):
        print('Name:', self.name, '\nYear:', self.yearob, '\nGender:', self.gender)
        
    def gender_retirement(self):
        if self.gender == 'Male':
         return print('Can be retired after 65 years old')
        else: 
            print('Can be retired after 55 years old')
class Employee(Person):
    def __init__(self, name, yearob, gender, employee):
        super().__init__(name, yearob, gender)
        self.employee=employee
    def display1(self):
        print('Name:', self.name, 'Age:', self.yearob, 'Type:', self.employee, '\nGender:', self.gender)
class Student(Person):
    def __init__(self, name, yearob, gender, student):
        super().__init__(name, yearob, gender)
        self.student=student
    def display2(self):
         print('Name:', self.name, 'Age:', self.yearob, 'Type:', self.student, '\nGender:', self.gender)
         

user1=Person('Juan', 1996, 'Male')
user1.display()
user1.age_calculation()
user1.gender_retirement()

user2= Employee('Tony', 1995, 'Female', 'Employee')
user2.display1()
user2.age_calculation()
user2.gender_retirement()

user3= Student('Don', 1994,'Male', 'Student')
user3.display2()
user3.age_calculation()
user3.gender_retirement()