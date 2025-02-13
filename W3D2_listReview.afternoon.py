#W3D2 - List Review-1Dimensional Lists & Parallel Lists


# PROMPT: Our demo will  focus on reviewing accessing text  fiel data and storing he daat inot 1d lisst . We will store the fiel data inot respective lists , the process the data to print the info for each student as well as calculate and stre a new piece of data for each student :




# this file uses: class_grades.csv

#IMPORTS------------------------------------

import csv 
#FUNCTIONS------------------------------------

#--MAIN EXECUTING CODE----------------------------
#initilaize a record counting variable
total_records = 0

# cretae an empty list for every potential field
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []
#connecting to file 
with open ("class_grades.csv")  as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        #count variable data
        total_records += 1 

       # store value to a friendly name
        #fname = rec[0]

        #print(fname)

        #store data from current record to corresonding lists
        #, append () ---> adds the data to the next avaialbe space in the list 

        #parallel lists ---> data dispresedx across lists, connectd by th esame index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#disconnected from file

#processing lists --- USE A FOR LOOP


#ceate a new list to hold each student's average test score
avg = []

for i in range(0, len(test1)):

    a = (test1[i]  + test2[i] + test3[i]) / 3
    avg.append(a)

print(f"INDEX #: {'FIRST':10} {'LAST':10} {'T1':3} {'T2':3} {'T3':3} {'AVG'}")
print("------------------------------------------------------------------------------------------------)")

for index in range(0, len(firstName)): #is a funtion
#for very itme , index will start at 0 and run up to (not including) he length (# of items)
    print(f"INDEX {index}: {firstName[index]:10}  {lastName[index]:10}  {test1[index]:3}  {test2[index]:3}  {test3[index]:3} {avg[index]:.2f}")
print("-----------------------------------------------------------------------------")

total_avg = 0

for i in range(0,len(avg)):
    total_avg += avg[i]

    class_avg = total_avg / len(avg)

print(f"\nTOTAL RECORDS: {total_records}\n CURRENT CLASS AVERAGE: {class_avg:.2f}\nGOODBYE!")
