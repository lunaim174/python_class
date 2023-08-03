# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 1 -------------------------------------      

#Importing needed libraries/modules
from country import Country
import re
from operator import attrgetter

# Printing title
print('----------------COUNTRIES POPULATION----------------')

#Define list
countries= []

#Reads the external 'data.txt' file
data = open('data.txt', 'r')

#Create Country instances from the read file
for line in data:
    wordlist = re.split(r'\t+', line.rstrip()) #line.split()
    countries.append(Country(wordlist[0],float(wordlist[1].replace(',','')),float(wordlist[2].replace(',',''))))

#Sort countries by population
sortedElements= sorted(countries, key=attrgetter('population'), reverse = True)

#Print the sorted elements
for country in sortedElements:
    country.display()

    
