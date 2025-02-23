# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 20:24:34 2022

@author: Andres Valdes
"""


class Car():
    def __init__(self, colour='NA', brand='NA', topSpeed=0, currentSpeed=0, up=0, down=0):
        self.colour= colour
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
        print('Car color is:', my_car.colour,'\nBrand: ', my_car.brand,\
              "\nMax speed:", my_car.topSpeed, '\nCurrent speed:', my_car.currentSpeed)


my_car = Car('red','Hundai',100,80, 50, 5)#Enter the values
my_car.start()
my_car.accelerate()
my_car.brake()
my_car.display()
