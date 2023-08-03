# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 1 - Question 4 -------------------------------------
# Printing title
print('----------Salary Calculator----------');

#Declare constants
BASE_HOURS = 40;
OVERTIME_FACTOR = 1.5;


# Ask Employee name
v_name = input('Enter Employee name: ');

# Ask Hourly Wage
v_rate = float(input('Enter the hourly rate: '));

# Ask Number of Hours worked
v_hours = float(input('Enter the number of hours worked:'));

# Use if-elif-else to calculate the salary
if v_hours <=BASE_HOURS:
   v_total = v_hours * v_rate;
else: 
   v_total = (BASE_HOURS * v_rate) + ((v_hours - BASE_HOURS)*(v_rate*OVERTIME_FACTOR));

# Print a paycheck for the Employee
print('----------Paycheck----------');
print('Employee:', v_name);
print('The pay will be $%.2f for %.2f hours of work.' %(v_total, v_hours));

