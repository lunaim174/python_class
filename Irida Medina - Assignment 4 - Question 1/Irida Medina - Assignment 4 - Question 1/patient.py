# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 4 - Question 1 -------------------------------------
# This module defines the class Patient

## Constructs the class Patient
class Patient:
    def __init__(self, first, middle, last, address, city, state, zipcode, phone, ename, ephone):
        self.__first = first
        self.__middle = middle
        self.__last= last
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__phone = phone
        self.__ename = ename
        self.__ephone = ephone

### Accesor methods:
## Gets the first name of the patient:
#  @return the first name
    def getFirst(self):
        return self.__first
  
## Gets the middle name of the patient:
#  @return the middle name
    def getMiddle(self):
        return self.__middle
  
## Gets the last name of the patient:
#  @return the last name
    def getLast(self):
        return self.__last

## Gets the address of the patient:
#  @return the address
    def getAddress(self):
        return self.__address
  
## Gets the city of the patient:
#  @return the city
    def getCity(self):
        return self.__city
  
## Gets the state of the patient:
#  @return the state
    def getState(self):
        return self.__state
  
## Gets the zipcode of the patient:
#  @return the zipcode
    def getZipCode(self):
        return self.__zipcode
  
## Gets the phone of the patient:
#  @return the phone
    def getPhone(self):
        return self.__phone

## Gets the name of the emergency contact of the patient:
#  @return the name of the emergency contact
    def getEName(self):
        return self.__ename
  
## Gets the phone of the emergency contact of the patient:
#  @return the phone of the emergency contact
    def getEPhone (self):
        return self.__ephone
   
### Mutator Methods
## Changes the first name of the patient:
    def updFirst(self, first):
        self.__first = first
  
## Changes the middle name of the patient:
    def updMiddle(self, middle):
        self.__middle = middle
  
## Changes the last name of the patient:
    def updLast(self, last):
        self.__last = last

## Changes the address of the patient:
    def updAddress(self, address):
        self.__address = address
  
## Changes the city of the patient:
    def updCity(self, city):
        self.__city = city
  
## Changes the state of the patient:
    def updState(self, state):
        self.__state = state
  
## Changes the zipcode of the patient:
    def updZipCode(self, zipcode):
        self.__zipcode = zipcode
  
## Changes the phone of the patient:
    def updPhone(self, phone):
        self.__phone = phone

## Changes the name of the emergency contact of the patient:
    def updEName(self, ename):
        self.__ename = ename
  
## Changes the phone of the emergency contact of the patient:
    def updEPhone(self, ephone):
        self.__ephone = ephone
   
