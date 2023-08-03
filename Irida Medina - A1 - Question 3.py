# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 1 - Question 3 -------------------------------------
# Printing title
print('----------Tip Calculator----------');

# Printing the satisfaction level scale
print('Please use the following scale:');
print('1: Totally satisfied');
print('2: Satisfied');
print('3: Dissatisfied');

# Ask the user their level of satisfaction and bill
v_level = int(input('What was your level of satisfaction today?'));
v_bill = float(input('Also, how much was your bill?'));

# Use if-elif-else to calculate and print the tip
if v_level == 1:
    print('Because you were totally satisfied, your tip should be $%.2f' %(v_bill*0.2));
elif v_level == 2:
    print('Because you were satisfied, your tip should be $%.2f' %(v_bill*0.15));
elif v_level == 3:
    print('Because you were dissatisfied, your tip should be $%.2f' %(v_bill*0.1));
else: print('The level of satisfaction you indicated is invalid.');


