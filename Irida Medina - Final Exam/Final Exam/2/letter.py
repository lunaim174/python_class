# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 2 -------------------------------------      
# This module defines the class Letter

## Constructs the class Letter
class Letter:
    def __init__(self, letterFrom, letterTo):
        self.__letterFrom = letterFrom
        self.__letterTo = letterTo
        self.__body = []

###Define Methods:
## Adds a line of text to the body of the letter
    def addLine(self, line):
        self.__body.append(line)
        
## Returns the entire text of the letter
    def getText(self):
        print('Dear', self.__letterTo + ': \n')
        for line in self.__body:
            print(line)
        print('')
        print('Sincerely,\n')
        print(self.__letterFrom)
        
        