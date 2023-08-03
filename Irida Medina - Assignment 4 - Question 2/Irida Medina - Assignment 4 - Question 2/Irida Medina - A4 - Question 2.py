# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #

# Assignment 4 - Question 2 -------------------------------------
# This program generates two objects from CashRegister

#Importing the two classes, and the datetime module
from cashregister import CashRegister

# Create first object:
object1 = CashRegister(7.5)
object1.addItem(10,False)
object1.addItem(19.55,True)

# Create second object:
object2 = CashRegister(11.2)
object2.addItem(20,False)
object2.addItem(11.2,True)
object2.addItem(3,True)

print('---- Cash Register transactions: ----')
print('First Object')
print('Total items for first object: ', object1.getCount())
print('Total price for first object: ', object1.getTotal())
print('-------------------------------------')
print('Second Object')
print('Total items for first object: ', object2.getCount())
print('Total price for first object: ', object2.getTotal())

