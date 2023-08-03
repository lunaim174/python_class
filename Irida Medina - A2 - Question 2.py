# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 2 - Question 2 -------------------------------------
# Printing title
print('----------Organisms Size Population----------')

# Ask the user the starting number of organisms
v_number_of_organisms = float(input('What is the starting number of organisms? '))

#Verify the starting number of organisms is valid
while v_number_of_organisms < 1:
    print('The number of organisms is not valid.')
    v_number_of_organisms = float(input('What is the starting number of organisms? '))

# Ask the user the average daily population increase
v_increase = float(input('What is the average daily population increase? '))

#Verify the average daily population increase is valid
while v_increase < 0.01:
    print('The average daily population increase is not valid.')
    v_increase = float(input('What is the average daily population increase? '))

# Ask the user the number of days to multiply
v_days = int(input('What is the number of days they are going to be left to multiply? '))

#Verify the average daily population increase is valid
while v_days < 1:
    print('The number of days left to multiply is not valid.')
    v_days = int(input('What is the number of days they are going to be left to multiply? '))

#Calculate and print results
print('Day ---------------------- Approximate Population')
for day in range(v_days): 
    print(day+1, ' ---------------------- ', v_number_of_organisms)
    v_number_of_organisms += ((v_number_of_organisms * v_increase)/100)    