#Saniyyah Shaheed
#Midterm_ Practical_Part_2
#SE126.02
#2_10_25

#PROGRAM PROMPT:Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold an office number for each of the employees. Office numbers should start at 100 and not exceed 200. Assign each employee an office number and store to the newly created list, then process through the six lists to display all of the data to the user as well as the total number of records in the file. Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice1.csv’, where each employee’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay). Finally, create a sequential search program that allows a user to repeatedly search the employee information stored in the lists based on the following menu: Westeros Services Directory Search 1.Search by EMAIL 2.Search by DEPARTMENT 3.EXIT.
# *For option 1: When a searched-for item is found, print all data* in the program on the specific employee from the lists. If they are not found, alert the user. For option 2: When a searched for item is found, print all data* in the program on all employees that match the criteria. If no one matches the searched-for criteria, alert the user.  
#------------------------------------------------------->
#VARIABLE DICTIONARY:

#---IMPORTS------------------------------------------------>

import csv
#--------------------------------------------------------->
#initialize variables needed to be counted
total_records = 0
#---------EXECUTING MAIN CODE----------------------------------------------------------------->
#--------create an empty list for each field data------------------------------------------------------------>
first_Name = []     #field 0
last_Name = []      #field 1
eMail = []          # field 2
deparTment = []     # field 3
phone_Ext = []      # field 4
office_Number = []  # field 5

#------#CONNECTING TO FILE------------------------------------------------------------------------>
with open("westeros.csv") as csvfile:
    file = csv.reader(csvfile)
    
    for rec in file:
        #store data from current record to corresponding lists (each field is its own!)
        #.append() --> adds the data to the next available space in the list (end)

        #parallel lists --> data dispersed across lists, connected by the same index
        first_Name.append(rec[0])
        last_Name.append(rec[1])
        eMail.append(rec[2])
        deparTment.append(rec[3])
        phone_Ext.append(int(rec[4]))
        

#--------------Disconnect from file---------------->
#process the lists to create and store office numbers to each employee starting from 100,then display all data back to the user
office_Number = [] # field 5
count = 100

for i in range(0, len(first_Name)):
    office_Number.append(count)
    count += 1

#print field headers for display below
print(f"{'FIRST':10}  {'LAST':10}       {'EMAIL':25}        {'DEPARTMENT':20}        {'PHONE EXT':3}     {'OFFICE #':3} ")
print("----------------------------------------------------------------------------------------------------------------------------")

#process through 6 lists for display
for i in range(0, len(first_Name)):
    print(f"{first_Name[i]:10}     {last_Name[i]:10}    {eMail[i]:25}       {deparTment[i]:20}    {phone_Ext[i]:3}  {office_Number[i]:3}")
print("----------------------------------------------------------------------------------------------------------------------------------")
print(f"TOTAL RECORDS IN FILE: {len(first_Name)}")

#-----------------SEQUENTIAL SEARCH-------------------------------------------------------------------
#build a repeatable program that allows a user to search for employee info stored in lists based on following menu
print("\tWesteros Services Directory Search:")

answer = input("Would you like to start your search? [y/n]: ").lower()

while answer == "y":
    #display user search menu 
    print("\t~Search Menu~")
    print("1. Search by EMAIL")           #one search value found
    print("2. Search by DEPARTMENT")      #multiple search values found
    print("3. EXIT")
    #gain search type 
    search_type = input("Enter your search type [1-3]: ")

    #filter search options based on type
    if search_type == "1": #EMAIL
        #sequential search - search for an employee by their EMAIL
        print("\tEMAIL SEARCH~")
        #set-up and gain search query
        found = -1  
        search_email = input("Enter the email you wish to find: ") # email we are looking for
        #perform search algo
        for i in range(0, len(eMail)):
            if search_email.lower() == eMail[i].lower(): 
                found = i  
        #display results to user; both for found or NOT found
        if found != -1:
            #email FOUND!
            print(f"Your search for {search_email} was FOUND! Here is their data: ")
            print(f"{first_Name[found]:10}  {last_Name[found]:10}  {eMail[found]:25}  {deparTment[found]:20}  {phone_Ext[found]:3}  {office_Number[found]:3}")
        else: 
            #NOT found
            print(f"Your search for {search_email} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")

    elif search_type == "2": #LETTER GRADE
        print("\tDEPARTMENT SEARCH")

        #sequential search - search for an employee by their DEPARTMENt

        #set-up and gain search query
        found = []  #empty list, found locations (index) will be stored if/when found
        search_dept= input("Enter the DEPARTMENT you wish to find: ") #department we are looking through all employees for

        #perform search algo
        for i in range(0, len(deparTment)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_dept.upper() == deparTment[i]: 
                found.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple students whose letter grade fits the searched for grade
                print(f"Found a {search_dept} department in INDEX {i}")

        #display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {search_dept} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            #last name FOUND!
            print(f"Your search for {search_dept} was FOUND! Here is their data: ")

            for i in range(0, len(found)):
                print(f"{found[i]}:  {first_Name[found[i]]:10}  {last_Name[found[i]]:10}  {eMail[found[i]]:25}  {deparTment[found[i]]:20}  {phone_Ext[found[i]]:3}  {office_Number[found[i]]:3} ")
    #last option exit          
    elif search_type == "3": #exit
        print("\t~EXIT~")
        answer = "x"
    else:
        print("\t!INVALID ENTRY!")
    #build a way out of the loop 
    if search_type == "1" or search_type == "2":
        #when search_type == "3" the user has chosen to exit, and if they did not provide a 1, 2, or 3 to search_type then they will automatically be brought back through the loop to see the menu again
        answer = input("Would you like to search again? [y/n]: ").lower()


print("\nThanks for using the search program. Goodbye!\n")


