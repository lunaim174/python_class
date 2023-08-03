# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 2 -------------------------------------      

#Importing needed libraries/modules
from letter import Letter

# Printing title
print('----------------WRITING LETTERS----------------')

#Create sample letter
letter = Letter('John', 'Mary')

#Adding lines
letter.addLine('How are you?')
letter.addLine('I really miss you!')

letter.getText()
    
