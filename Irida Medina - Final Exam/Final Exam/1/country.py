# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 1 -------------------------------------      
# This module defines the class Country

## Constructs the class Country
class Country:
    def __init__(self, name, population, area):
        self.__name = name
        self.population = population
        self.__area = area
        self.__density = float(population)/float(area)

###Define Methods:
## Display the objects on the list
    def display(self):
        #sorted(self, key=operator.attrgetter('__population'))
        print('%30s:%20s' %(self.__name, int(self.population)))
        
