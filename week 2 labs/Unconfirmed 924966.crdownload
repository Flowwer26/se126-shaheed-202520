#Saniyyah Shaheed
#W2D2 -Lab #2- Text File Handling 
#1_21_25

#PROGRAM PROMPT:You have been asked to produce a report that lists all the computers in the csv filefilehandling.csv. Your report should look like the following sample output. The last line should print the number of computers in the file.

# VARIABLE DICTIONARY:#--IMPORTS-------------------------------------------------------->

import csv

#-------------------------MAIN CODE------------------------------------------------------->
#initialize needed counting variables
total_records = 0

# cretae an empty list for every potential field
machineType = []
brandType = []
computerNumber = []
storageSize = []
firstD = []
noH = []
secondD = []
operatingS = []
dateY = []

#-----connect filehandling to file------------------------------------->
with open("filehandling.csv") as csvfile: 
    #we must indent one level while "connected to the file"

    file = csv.reader(csvfile)

    for rec in file:
        #count variable data
        total_records += 1

        #assign each field data value to a friendly var name 
        type = rec[0]
        if type == "D":
            type = "Desktop"

        else:
            type ="Laptop"

        if second_disk
        else:
             
        if os
        else:
             
        if year:
             

        brand = rec[1] #all text data read as a string, so cast as a num!
        cpu = str(rec[2])
        ram = int(rec[3])
        first_disk = str(rec[4])
        no_hdd = int(rec[5])
        second_disk = str(rec[6])
        os = str(rec[7])
        yr = str(rec[0])

print(f"{'TYPE':5}   {'BRAND':5}   {'CPU':5}  {'RAM':5}  {'1st Disk':10}  {'No HDD':5}  {'2nd Disk':10}  {'OS':5}  {'YR':5} ") ##FIELD titles for table
print("-----------------------------------------------------")

   

        print(f"{type:5}   {brand:5}   {cpu:5}  {ram:05}  {first_disk:10}  {no_hdd:5}  {second_disk:10}  {os:05}  {yr:5}")

    

#-----connected to file--------
#display final data (counting vars)
print("-----------------------------------------------------")
print(f"Total computers in file: {total_records}\n\n")

