#W2D1

#STep 1 import the csv 
import csv


total_records = 0 #holdd total num of recs in file

#----------------connected to file------
# inclde relative fiule path in open()                                               
#  -make sure to flip escape sequence \ to / 
with open ("simple.csv") as csvfile:
    #make sure to indent inside code block 


    #allow the csv. reader tp access and read the filepath; stores cotent to "file" [a 2d list/ matrix/table]
    file = csv.reader(csvfile)

    print(f"{'NAME':10} {'NUM':10} {'COLOR':10}")
    print()
    #STEP 3: process through every record (row) in the file
    for record in file:
        #add +1 to total records to keep accurate  count  of of recs
        total_records +=1
        #print(record) #entire record/row data as a list

        name = record[0] #name field
        number = record [1] #record field
        color = record [2] # color field
        
        print(f"{name:10} {number:10} {color:10}")
##disconnected from file
print(f"TOTAL RECORDS: {total_records}\n")



