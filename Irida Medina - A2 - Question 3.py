# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 2 - Question 3 -------------------------------------

#Import libraries
import random

#Play Game Function
def playGuessingGame(v_quit):
    #Initialize variables
    v_restart = 1
    
    while v_quit == 0:    
        if v_restart == 1:
            #Generate random number to guess
            v_random = random.randint(1,10)
            print('Welcome to the Guessing Game!')
            v_restart = 0
            
            #Ask the user to guess the number
            v_number = int(input('Enter a number between 1 and 10, or 0 to quit: '))
            
            #Verify the number is within the range
            while v_number not in range(0,11):
                print('The number is not valid.')
                v_number = int(input('Enter a number between 1 and 10, or 0 to quit: '))
                
            #Check the number the user entered
            if v_number == 0:
                #print('Thanks for playing!')
                v_quit = 1
                return print('Thanks for playing!')
            elif v_number == v_random:
                print('Congratulations! You guessed the right number!')
                v_restart = 1
            elif v_number > v_random:
                print('Too high, try again')
            else:
                print('Too low, try again')
                
    
def main():
    # Printing title
    print('----------Guessing Game----------')
    v_quit = 0
    playGuessingGame(v_quit)
        
main()