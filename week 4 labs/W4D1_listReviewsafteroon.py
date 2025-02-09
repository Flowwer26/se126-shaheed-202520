#w4D1- sEQUETIAL sEARCH

#PROMPT:

#IMPORTS---------------------------------------------------------
import csv

#FUNCTIONS-------------------------------
def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let ="B"
    elif num >= 70:
        let = "C"
    elif num >= 60:
        let = "D"
    elif num < 60:
        let = "F"
    else: 
        let ="ERROR"

    return let #the let value will literaly repacethe letter() call in main code
#----------------------MAIN EXECUTING CODE------------------------

#Create empty list for every potential field in the file
firstName = []
lastName = []
test1 = []
test2 = []
test3 = []
#--------------connecting to file---------------------------------------- 
with open ("class_grades.csv")  as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        #store data from current record to corresonding lists(each field is its own)
        #, append () ---> adds the data to the next avaialbe space in the list (end)

        #parallel lists ---> data dispesed across lists, connectd by the same index
        firstName.append(rec[0])
        lastName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

#-------------disconnected from file-----------------------

#process the lists to create ans store each students numric average as well a letter grade average , the display all dat back to the user
num_avg = []
let_avg = []

for i in range(0, len(firstName)):
    a = (test1[i] + test2[i] + test3[i]) / 3
    num_avg.append(a)
    let_avg.append(letter(a))

#print field headers fro dispaly
print(f"{'FIRST':10} {'LAST':10} {'T1':3} {'T2':3} {'T3':3} {'# AVG'} {'L AVG'}")
print("------------------------------------------------------------------------------------------------------")
#processing through list for display
for i in range(0, len(firstName)):
    print(f" {firstName[i]:10}  {lastName[i]:10}  {test1[i]:3}  {test2[i]:3}  {test3[i]:3} {num_avg[i]:6.1f} {let_avg[i]}")
print("------------------------------------------------------------------------------------------------------")
print(f"TOTAL STUDENTS IN FILE : {len(firstName)}")

# sequential search - search for student by their last name 
# step 1
found = -1 #flag avr, will be repalced wiht index position if name is found
search_last = input("Enter the last name you wish to find: ")

#step 2 perform search algo (seq. search_--> for loop w/ if statemnt)
for i in range(0, len(lastName)):


    if search_last.lower() == lastName[i].lower():
        #if performs the SEARCH- is what we're ooking for here in the list?

        found = i #stores found item index LOCATION

#step 3 display result to user; make sure you give info: both for found or NOT found
if found != -1:
#lst name FOUND!
    print(f"Your seearch for {search_last} was FOUND! Here is their data: ")
    print(f"{firstName[found]:10}  {lastName[found]:10}  {test1[found]:3}  {test2[found]:3}  {test3[found]:3} {num_avg[found]:6.1f} {let_avg[found]}")

else:

#NOT FOUND
    print(f" Your search for {search_last} was not FOUND!")
    print("Chek your casting and spelling and try again!")

