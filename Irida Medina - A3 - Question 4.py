# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 3 - Question 4 -------------------------------------
# Printing title
print('----------Numbers----------')

#Initialize variables
numbers = []
total = 0

# Ask the user for 5 numbers
for number in range (1,6):
    value = float(input('Enter number %d of 5: ' %number))
    numbers.append(value)
    total += float(numbers[number-1])
    
low = min(numbers)
high = max(numbers)
average = total/5

    
print ('Low: %.2f' %low)
print ('High: %.2f' %high)
print ('Total: %.2f' %total)
print ('Average: %.2f' %average)

