# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 2 - Question 4 -------------------------------------      

# Printing title
print('----------Cash Balance----------')

# Ask the user for the variables
v_opening = float(input('Please enter the opening cash balance: '))
v_closing = float(input('Please enter the closing cash balance: '))
v_file = input('Please enter the file name: ')

#Opening file
inputFile = open(v_file, 'r')

#Calculating balance
for line in inputFile:
    parts = line.split()
    if parts[2] == 'R':
        v_opening += float(parts[1])
    else:
        v_opening -= float(parts[1])

if v_opening == v_closing:
    print('The closing balance is correct.')
else:
    print('The closing balance didn\'t match.')
    print('According to the file, it should be', v_opening)
    
inputFile.close()