# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 3 - Question 2 -------------------------------------
# Printing title
print('----------Counting Letters----------')

# Ask the user for the input file name
v_file = input('Enter filename: ')

#Opening file
inputFile = open(v_file, 'r')
text1 = inputFile.read()
inputFile.close()

#Initialize variables
uppercase = 0
lowercase = 0
digits = 0
spaces = 0

#Counting characters in the text
for character in text1:
    if character.isupper():
        uppercase +=1
    elif character.islower():
        lowercase +=1
    elif character.isdigit():
        digits +=1
    elif character.isspace():
        spaces +=1

#Print results
print('------------------------------------')
print('Uppercase letters:', uppercase)
print('Lowercase letters:', lowercase)
print('Digits:', digits)
print('Spaces:', spaces)
