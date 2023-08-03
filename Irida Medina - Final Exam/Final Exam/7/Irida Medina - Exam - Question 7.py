# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 7  -------------------------------------      

#Importing needed libraries/modules
import random

# Printing title
print('----------------THE CAPITAL\'S GAME----------------')

#Initializing dictionary with capital and states
states = {'Alabama':        'Montgomery',
          'Alaska':         'Juneu',
          'Arizona':        'Phoenix',
          'Arkansas':       'Little Rock',
          'California':     'Sacramento',
          'Colorado':       'Denver',
          'Connecticut':    'Hartford',
          'Delaware':       'Dover',
          'Florida':        'Tallahassee',
          'Georgia':        'Atlanta',
          'Hawaii':         'Honolulu',
          'Idaho':          'Boise',
          'Illinois':       'Springfield',
          'Indiana':        'Indianapolis',
          'Iowa':           'Des Moines',
          'Kansas':         'Topeka',
          'Kentucky':       'Frankfort',
          'Louisiana':      'Baton Rouge',
          'Maine':          'Augusta',
          'Maryland':       'Annapolis',
          'Massachusetts':  'Boston',
          'Michigan':       'Lansing',
          'Minnesota':      'Saint Paul',
          'Mississippi':    'Jackson',
          'Missouri':       'Jefferson City',
          'Montana':        'Helena',
          'Nebraska':       'Lincoln',
          'Nevada':         'Carson City',
          'New Hampshire':  'Concord',
          'New Jersey':     'Trenton',
          'New Mexico':     'Santa Fe',
          'New York':       'Albany',
          'North Carolina': 'Raleigh',
          'North Dakota':   'Bismarck',
          'Ohio':           'Columbus',
          'Oklahoma':       'Oklahoma City',    
          'Oregon':         'Salem',
          'Pennsylvania':   'Harrisburg',
          'Rhode Island':   'Providence',
          'South Carolina': 'Columbia',
          'South Dakota':   'Pierre',
          'Tennessee':      'Nashville',
          'Texas':          'Austin',
          'Utah':           'Salt Lake City',
          'Vermont':        'Montpelier',
          'Virginia':       'Richmond',
          'Washington':     'Olympia',
          'West Virginia':  'Charleston',
          'Wisconsin':      'Madison',
          'Wyoming':        'Cheyenne'
    }

print('Welcome to The Capital\'s Game!\n')

#Initialize variables
guess_input = ''
correct_answers = 0
incorrect_answers = 0

while (guess_input != '0'):
    x = random.randint(0,50) 
    guess_input = input('What\'s the capital of %s? (or enter 0 to quit):' %([key for key in states.keys()][x]))
    answer = [value for value in states.values()][x]
    if guess_input != '0':
        if answer == guess_input:
            print('That is correct.')
            correct_answers += 1
        else:
            print('That is incorrect.')
            incorrect_answers += 1
        
print('\nYou had %i correct responses and %i incorrect responses.' %(correct_answers, incorrect_answers))
print('Thanks for playing!')