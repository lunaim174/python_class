# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 5  -------------------------------------      

#Importing needed libraries/modules
from country import Country
import re
from operator import attrgetter

# Printing title
print('----------------COUNTRIES STATS----------------')

#Define list
countries= []

#Reads the external 'data.txt' file
data = open('data.txt', 'r')

#Create Country instances from the read file
for line in data:
    wordlist = re.split(r'\t+', line.rstrip())
    countries.append(Country(wordlist[0],float(wordlist[1].replace(',','')),float(wordlist[2].replace(',',''))))

#Calculating the largest population
x = max(countries, key=attrgetter('population'))
print('Largest Population:', x.getName())

#Calculating the largest area
x = max(countries, key=attrgetter('area'))
print('Largest Area:', x.getName())

#Calculating the largest density
x = max(countries, key=attrgetter('density'))
print('Largest Population Density:', x.getName())


