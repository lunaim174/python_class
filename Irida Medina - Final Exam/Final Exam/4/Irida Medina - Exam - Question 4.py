# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 4  -------------------------------------      

# Printing title
print('----------------WORKING WITH WORDS----------------')

#Ask the user for the name of the file to open
file_name = input('Enter the name of the file to open: ')

#Initialize the dictionary
words = []
dict = {}

#Reading the input files
input_file = open(file_name, 'r')

#Getting the words in the file
for line in input_file:
    words += (line.lower()).split()

#Check from letter A to Z to build the dictionary
for abc in range(97,123):
    found = set()
    for word in words:
        if chr(abc) in word:
            found.add(word)
    dict[chr(abc)] = found
    
#Print the letters and the dictionary
for abc in range(97,123):
    print('Words containing', chr(abc).upper()+':')
    if (dict[chr(abc)]):
        print('\t'+ str(sorted(dict[chr(abc)])))
        
        