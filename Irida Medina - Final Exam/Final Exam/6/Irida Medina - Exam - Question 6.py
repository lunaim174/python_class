# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 6  -------------------------------------      

# Printing title
print('----------------FINDING WORDS----------------')

#Initializing dictionary
found_Words = {}

#Reads the external 'data.txt' file
input_file = open('Kennedy.txt', 'r')
num_line = 1
body = ''
outfile = open('index.txt', 'w')

#Creates a dictionary with the words and their respective lines
for line in input_file:
    words = line.split()
    
    for word in words:
        x = found_Words.get(word)
        num_set = set()
        if x is not None:
            num_set = set(x)
        num_set.add(num_line)
        found_Words[word] = num_set
    num_line +=1 

#Sorts the words in alphabetical order
sorted_words = sorted(found_Words.keys(), key=lambda x:x.lower())

#Prints the body of the file
for key in sorted_words:
    body = ''
    body = key +': ', found_Words[key]
    body = str(body)
    outfile.write(body + '\n')
    
#Close the file
outfile.close()

