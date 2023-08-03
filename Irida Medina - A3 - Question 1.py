# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 3 - Question 1 -------------------------------------
# Printing title
print('----------Unique Words----------')

# Ask the user for the input file name
v_file = input('Enter the name of the input file: ')

#Opening file
inputFile = open(v_file, 'r')
text1 = inputFile.read()
inputFile.close()

#Checking the unique words
word_list = text1.split()
unique_words = set(word_list)

#Print results
print('---------------------------------------')
print('These are the unique words in the text:')
for word in unique_words:
    print(word)
    