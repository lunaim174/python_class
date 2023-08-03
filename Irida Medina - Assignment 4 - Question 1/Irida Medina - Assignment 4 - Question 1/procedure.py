# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 4 - Question 1 -------------------------------------
# This module defines the class Procedure

## Constructs the class Procedure
class Procedure:
    def __init__(self, pname, pdate, practitioner, charges):
        self.__pname = pname
        self.__pdate = pdate
        self.__practitioner = practitioner
        self.__charges = charges

### Accesor methods:
## Gets the procedure's name:
#  @return the procedure name
    def getPName(self):
        return self.__pname
  
## Gets the procedure's date:
#  @return the procedure's date
    def getPDate(self):
        return self.__pdate
  
## Gets the practitioner name:
#  @return the practitioner name
    def getPractitioner(self):
        return self.__practitioner

## Gets the charges for the procedure:
#  @return the charges amount
    def getCharges(self):
        return self.__charges
     
### Mutator Methods:
## Changes the procedure's name:
    def updPName(self, pname):
        self.__pname = pname
  
## Changes the procedure's date:
    def updPDate(self, pdate):
        self.__pdate = pdate
  
## Changes the practitioner's name:
    def updPractitioner(self, practitioner):
        self.__practitioner = practitioner

## Changes the charges for the procedure:
    def updCharges(self, charges):
        self.__charges = charges
