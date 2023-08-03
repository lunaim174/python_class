# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #

# Assignment 4 - Question 1 -------------------------------------
# This program defines a patient and creates 3 procedures

#Importing the two classes, and the datetime module
from patient import Patient
from procedure import Procedure
from datetime import date

# Create an instance of the Patient class, initialized with sample data
patient1 = Patient('James','Edward', 'Jones','123 Main Street', 'Billings',
                   'Montana', '59000','406-555-1212','Jenny Jones', '406-555-1213')

# Create 3 instances of the Procedure class:
procedure1 = Procedure('Physical Exam',
                       date.today(),
                       'Dr. Irvine',
                       250
                       )

procedure2 = Procedure('X-ray',
                       date.today(),
                       'Dr. Jamison',
                       500
                       )

procedure3 = Procedure('Blood test',
                       date.today(),
                       'Dr. Smith',
                       200
                       )

print('---- Patient\'s Information: ----')
print('First Name: ', patient1.getFirst())
print('Middle Name: ', patient1.getMiddle())
print('Last Name: ', patient1.getLast())
print('Address: ', patient1.getAddress())
print('City: ', patient1.getCity())
print('State: ', patient1.getState())
print('ZIP: ', patient1.getZipCode())
print('Phone: ', patient1.getPhone())
print('Emergency Contact: ', patient1.getEName())
print('Emergency Phone: ', patient1.getEPhone())
print('')
print('Procedure: ', procedure1.getPName())
print('Date: ', procedure1.getPDate())
print('Practitioner: ', procedure1.getPractitioner())
print('Charge: ', procedure1.getCharges())
print('')
print('Procedure: ', procedure2.getPName())
print('Date: ', procedure2.getPDate())
print('Practitioner: ', procedure2.getPractitioner())
print('Charge: ', procedure2.getCharges())
print('')
print('Procedure: ', procedure3.getPName())
print('Date: ', procedure3.getPDate())
print('Practitioner: ', procedure3.getPractitioner())
print('Charge: ', procedure3.getCharges())
print('')
print('Total Charges: ', procedure1.getCharges()+procedure2.getCharges()+procedure3.getCharges())
