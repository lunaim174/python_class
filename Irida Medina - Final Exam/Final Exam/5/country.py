# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 5 -------------------------------------      
# This module defines the class Country

## Constructs the class Country
class Country:
    def __init__(self, name, population, area):
        self.__name = name
        self.population = population
        self.area = area
        self.density = float(population)/float(area)

###Define Methods:
## Gets the Country Name
    def getName(self):
        return self.__name
    
## Gets the Country Area
    def getArea(self):
        return self.__area

## Gets the Country Population
    def getPopulation(self):
        return self.__population

## Gets the Country Density
    def getDensity(self):
        return self.__density
    
    
    