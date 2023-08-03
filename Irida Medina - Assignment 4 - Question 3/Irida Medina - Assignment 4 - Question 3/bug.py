# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 4 - Question 3 -------------------------------------
# This module defines the class Bug

## Constructs the class Bug
class Bug:
    def __init__(self, initialPosition):
        self.__Position = initialPosition

###Define Methods:
## The bug moves to the right
    def move(self):
        self.__Position += 1
  
## The bug turns to the left
    def turn(self):
        self.__Position -= 1
  
## Gets the current position of the bug
    def getPosition(self):
        return self.__Position
        

