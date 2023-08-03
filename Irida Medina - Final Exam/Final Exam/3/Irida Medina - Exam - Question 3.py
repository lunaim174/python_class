# -*- coding: utf-8 -*-

# Class ISMN-6650-001
# Irida Medina #


# Exam 2 - Final - Question 3  -------------------------------------      

# Printing title
print('----------------WRITING JUNK MAILS----------------')

#Reading the input files
ftemplate = open('template.txt', 'r')
database = open('database.txt', 'r')

for line in database:
    data = line.split("|")
    ftemplate = open('template.txt', 'r')
    template = ftemplate.read()
    count = 1
    outfile = open(data[1]+data[2]+'.txt', 'w')
    #outfile.write(template)
    for elem in data:
        template = template.replace('|'+ str(count) +'|', elem.strip())
        count += 1
    outfile.write(template)
    outfile.close()
    
