# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 4 - Question 2 -------------------------------------
# This module defines the class CashRegister

## Constructs the class CashRegister
class CashRegister:
    def __init__(self, taxRate):
        self.__itemCount = 0
        self.__totalPrice = 0
        self.__taxableTotal = 0
        self.__taxRate = taxRate

###Define Methods:
## Clear all the transactions:
    def clear(self):
        self.__itemCount = 0
        self.__totalPrice = 0
        self.__taxableTotal = 0
        self.__taxRate = 0
  
## Gets the total items:
    def getCount(self):
        return self.__itemCount
  
## Gets the total price:
    def getTotal(self):
        if self.__taxableTotal >0:
            return round(self.__taxableTotal + self.__totalPrice,2)
        else:
            return round(self.__totalPrice, 2)

## Adds a new item:
    def addItem(self, price, taxable):
        self.__itemCount += 1
        self.__totalPrice += price 
        if taxable:
            self.__taxableTotal += (price * self.__taxRate/100)
     

