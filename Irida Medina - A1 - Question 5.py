# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 1 - Question 5 -------------------------------------
# Printing title
print('----------Magic Dates----------');

# Ask for the month
v_month = int(input('Enter the month in numeric form: '));
while (v_month not in range(0,13,1)):
    print ('Month is not valid.')
    v_month = int(input('Enter the month in numeric form: '));

# Ask for the day
v_day = int(input('Enter the day of the month: '));
if (v_month in (1,3,5,7,8,10,12)):
    while (v_day not in range(0,32,1)):
        print ('Day is not valid.')
        v_day = int(input('Enter the day of the month: '));
elif (v_month in (4,6,9,11)):
    while (v_day not in range(0,31,1)):
        print ('Day is not valid.')
        v_day = int(input('Enter the day of the month: '));
else: 
    while (v_day not in range(0,29,1)):
        print ('Day is not valid.')
        v_day = int(input('Enter the day of the month: '));

# Ask for the year
v_year = int(input('Enter the year in two digits format: '));
while (v_year not in range(-1,100,1)):
    print ('Year is not valid.')
    v_year = int(input('Enter the year in two digits format: '));

#Print the date
print ('The date is:',v_month,'/',v_day,'/',v_year);
if(v_month * v_day == v_year):
    print('This is a magic date.')
else: print ('This is not a magic date.')

