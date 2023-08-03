# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #

# Assignment 4 - Question 3 -------------------------------------
# This program generates two bugs from Bug

#Importing the two classes, and the datetime module
from bug import Bug

# Create first bug:
bug1 = Bug(5)
for i in range(5):
    bug1.move()
bug1.turn()

# Create second bug:
bug2 = Bug(6.3)
bug2.turn()
bug2.move()
bug2.move()

print('---- Bug Movements: ----')
print('Bug 1')
print('The current position for bug 1 is: ', bug1.getPosition())
print('-------------------------------------')
print('Bug 2')
print('The current position for bug 2 is: ', bug2.getPosition())

