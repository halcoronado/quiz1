''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode

infile = open("students.csv",'r')


# create a csv object from the file object
students = csv.reader(infile, delimiter=',')

#to skip a line if the file contains a header record
next(students)

#skip the header row


#create an outfile object for the pocessed record
outfile = open('processedStudents.csv','a')


#create a new dictionary named 'student_dict'
student_dict = {}


#use a loop to iterate through each row of the file

    #check if the GPA is below 3.0. If so, write the record to the outfile
    
    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA

for x in students:
    y = float(x[8])
    if y < 3.00:
        student_dict[x[0]] = y
    
    
    


#print the entire dictionary
print (student_dict)

#Print the student id 
for x in student_dict.items():
    print(x[0])
    outfile.write(str(x[0]))

#print out the corresponding GPA from the dictionary
for x in student_dict.items():
    print(x[1])
    outfile.write(str(x[1]))


#close the outfile



outfile.close()




