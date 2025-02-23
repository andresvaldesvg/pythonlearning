# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:40:34 2022

@author: Name: Andres David Valdes Gonzalez
ID: A00062146
"""


class Bike():
    def __init__(self, model='NA', brand='NA', topSpeed=0, currentSpeed=0, up=0, down=0):
        self.model= model
        self.brand= brand
        self.topSpeed= topSpeed
        self.currentSpeed = currentSpeed
        self.up = up
        self.down = down
     
#Methods
    def start(self):
        self.currentSpeed + self.currentSpeed
        return self.currentSpeed
    def accelerate(self):
        self.currentSpeed +=self.up
        return self.currentSpeed
    def brake(self):
        self.currentSpeed -=self.down
        return self.currentSpeed
    def stop(self):
        self.currentSpeed -=self.currentSpeed
        return self.currentSpeed

#Display the speed

    def display(self):
        print('Bike is:', self.model,'\nBrand: ', self.brand,\
              "\nMax speed:", self.topSpeed, '\nCurrent speed:', self.currentSpeed)


my_bike = Bike('Dr. bike X3434','Road',30,0, 20, 10)#Enter the values
my_bike.start()
my_bike.accelerate()
my_bike.brake()
my_bike.display()

print('\nSecond object: \n')

my_bike2 = Bike('Super bike X3422','Downhill',50,0, 20, 10)#Enter the values
my_bike2.start()
my_bike2.accelerate()
my_bike2.brake()
my_bike2.display()