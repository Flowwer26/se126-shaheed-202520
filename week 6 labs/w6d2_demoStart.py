#W6D2 - Binary Search + Bubble Sort

#this file uses: party.csv 

#PROGRAM PROMPT: Build a repeatable, menu-driven program to access and search for data within the file

#--IMPORTS-------------------------------------------------------------------------------
import csv

#--FUNCTIONS-----------------------------------------------------------------------------
def display(x, records):
    '''
        PARAMETERS:
            x   signifier for if we are printing a single record or multiple
                when x != "x" it is an integere index and we have one value, otherwise we have multiple

            records   the length of a list we are going to process through (# of loops/prints)
    '''
    print(f"{'CLASS':8}  {'NAME':10}  {'MEANING':25}  {'CULTURE'}")
    print("----------------------------------------------------------------")
    if x != "x":
        #printing one record
        print(f"{class_type[x]:8}  {name[x]:10}  {meaning[x]:25}  {culture[x]}")

    elif found:
        #printing multiples, based on length stored in 'foundList'
        for i in range(0, records):
            print(f"{class_type[found[i]]:8}  {name[found[i]]:10}  {meaning[found[i]]:25}  {culture[found[i]]}") 
    
    else:
        #printing full data, based on length stored in 'records'
        for i in range(0, records):
            print(f"{class_type[i]:8}  {name[i]:10}  {meaning[i]:25}  {culture[i]}")

    print("----------------------------------------------------------------\n")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp
    
#--MAIN EXECUTING CODE-------------------------------------------------------------------
practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]

class_type = []
name = []
meaning = []
culture = []

found = []
with open("party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])
#disconnected from file------------------------------------

#display whole list data to user
display("x",len(class_type)) #practice with function

display(16, len(name))

ans = input("Would you like to enter the search program? [y/n]").lower()

#validity and user error trap loop
while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter the search program? [y/n]").lower()

#main searching loop
while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Search by TYPE") #shows all of either elf or dragon
    print("2. Search by NAME") #binary search review
    print("3. Search by MEANING") #find part of a whole (sequential search)
    print("4. EXIT")              #continually repeat until exit
    search_type = input("\nHow would you like to search today? [1-4]: ")

    #using 'not in' for user validity checks
    if search_type not in ["1", "2", "3", "4"]:#or menu_options:
         print("***INVALID ENTRY!***\nPlease try again") #when user doesnt listen to directions will see this message
    
    elif search_type == "1":
        print(f"\nYou have chosen to search by TYPE")
        
        #allow the user to search for a certain TYPE and then display ALL records (multi) with that type
        search = input("Which type: 'dragon' or 'elf':")

        #show all values of dragon or elf--->> squential search 
        if search.lower() not in ["dragon" , "elf"]:
            print("Sorry,only 'dragon' or 'elf' are accepted.Please try again.")
        
        else:
            #sequential search for MULTIPLE VALUES MATCHING SEARCH TERM
            found = []

            for i in range(0, len(class_type)):
                if search == class_type[i].lower():
                    found.append(i) #add current index (location) of found item to 'found' list
                
            if not found: #if the found list is still empty
                print(f"Sorry,your search for {search} came up empty.")
            
            else:
                #call display to show the values
                display("x", len(found))


    elif search_type == "2":
        print(f"\nYou have chosen to search by NAME")


        #allow the user to search for ONE specific and unique name value (binary search!)
        search = input("Enter the NAME you are looking for: ")
        #BINARY SEARCH: 
        #               * requires a collection of UNIQUE values to search through
        #               * requires the collection to be SORTED (ORDERED)
        #                       ascending or descending ; alpha or numeric

        #Bubble sort --> higher values 'bubble' to the bottom of the collection
        for i in range(0, len(name) - 1):
            for j in range(0, len(name) - 1):
                if name[j] > name[j + 1]:
                    #they must swap places because the higher value must come afterwards
                    temp = name[j]
                    name[j] = name[j + 1]
                    name[j + 1] = temp

                    #use the function to cut down on coding and potential errors!
                    swap(j, class_type)
                    swap(j, meaning)
                    swap(j, culture)


        #check our bubble sort -- sorting in ascending order by name
        display("x", len(name))

        
                

        

        #BINARY SEARCH: must be ermd on orderedor sortd list popu;lated with unique values - can only find one item or value 

        min = 0             #lowest possible index
        max = len(name) - 1 #highst index
        mid = int((min + max) /2) #middle index inn sorted list 
        

        while min < max and search.lower() != name[mid].lower():

            if search.lower() < name[mid].lower():
                max = mid - 1
            else:
                #search> name[mid]
                min = mid + 1
            mid = int((min + max) /2)
        
        if search.lower() == name[mid].lower():
            print(f"Huzzah! we have found your searrch for {search}, see details below:")
            display(mid, len(name))
        else:
            print(f"Sorry, we could  not find your search for {search}. Please try again.")

    elif search_type == "3":
        print(f"\nYou have chosen to search by MEANING")

        search = input("Which name meaning are you looking for:").lower()
        
        #allow the user to search for a KEYWORD within the meaning[] values
       

    elif search_type == "4":
        print(f"\nYou have chosen to EXIT")
        ans = "N"

#alert user that program is about to end
print("Thank you for using my program, goodbye!\n")