# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Assignment 2 - Question 1 -------------------------------------
# Printing title
print('----------Rainfall Calculation----------')

# Ask the user how many years they want to calculate
v_number_of_years = int(input('How many years do you want to calculate?'))

#Verify the number of years is valid
while v_number_of_years < 1:
    print('The number of years is not valid.')
    v_number_of_years = int(input('How many years do you want to calculate?'))

#Initialize variables0
v_total_quarters = 0
v_total_rainfall = 0
# Iterate for the number of years, and ask for the rainfall 4 times (one per quarter)
for year in range(v_number_of_years):
    print('-- For year', year+1, ':')
    for quarter in range(4):
        v_text = 'Enter the rainfall for the quarter number ' + str(quarter+1) + ':'
        v_rainfall = float(input(v_text))
        v_total_rainfall += v_rainfall
        v_total_quarters+=1
        
# Print totals and calculate the average
print('Total number of quarters:', v_total_quarters)
print('Total rainfall in', v_number_of_years, ':', v_total_rainfall)
print('Average quarterly rainfall:', round((v_total_rainfall/v_total_quarters),2), 'inches');


