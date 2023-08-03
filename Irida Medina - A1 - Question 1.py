# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 1 - Question 1 -------------------------------------
# Printing title
print('----------Cookies Recipe----------');

# Ask the user how many cookies they want
v_number_of_cookies = float(input('How many cookies do you want to bake?'));

# Printing the number of cookies the user wanted
print('--These are the ingredients you need for', v_number_of_cookies, 'cookies:');

# Calculate every ingredient using a mathematical rule of three, 
# and printing only two decimal points
print('%.2f cups of sugar' %((v_number_of_cookies*1.5)/48));
print('%.2f cups of butter' %((v_number_of_cookies*1)/48));
print('%.2f cups of flour' %((v_number_of_cookies*2.75)/48));


