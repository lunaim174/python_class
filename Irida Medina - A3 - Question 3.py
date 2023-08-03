# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 3 - Question 3 -------------------------------------
# Printing title
print('----------Pig Latin----------')

# Ask the user for a sentence to 'translate'
v_sentence = input('Enter a string: ')

#Initialize variables
sentence_words = []
translation = ''

#Apply the Pig Latin conditions
sentence_words = v_sentence.split()

for word in sentence_words:
    translation += word[1:len(word)] + word[0] + 'ay '
    
#Print results
print('-----------------------------')
print('Pig Latin of your input: ', translation.upper())

