# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 1 - Question 2 -------------------------------------
# Printing title
print('----------Largest of the three numbers----------');

# Ask the user for the three numbers and assign them as float
v_number_1 = float(input('Enter the first number: '));
v_number_2 = float(input('Enter the second number: '));
v_number_3 = float(input('Enter the third number: '));

# Use if-elif-else to find the largest number
if (v_number_1>v_number_2):
    v_max = v_number_1
elif (v_number_2>v_number_3):
    v_max = v_number_2
else: v_max = v_number_3;

#Print the result
print('The largest number is: %.1f' %v_max);

