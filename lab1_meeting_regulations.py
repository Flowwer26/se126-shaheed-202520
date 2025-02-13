#Saniyyah Shaheed
#1_14_2025
#Lab_1_202520
#W2D1
#SE_126_02

#PROGRAM PROMPT:  Build a function that is passed both the number of people attending the meeting, as well as the maximum room capacity. This function should determine the number of people over/under the capacity based on these two values, and return the difference value

#VARIABLE DICTIONARY
#mx_cap             max capacity of room (= 50)
#ppl_attend         number of people attending by user
#ppl_over           number of people over capacity (mx_cap > 50)
#ppl_under          number of people under capacity (mx_cap < 50)
#total_pplattend    (mx_cap - ppl_attend)
#ddiff_totalppl_ovr_remove  number of people over capacity to remove (ppl_over - mx_cap)
#diff_totalppl_undr_add number of people under capacity to add (mx_cap - ppl_under)
#answer             loop control; value determines if loop repeats, entered by the user

#--------------------FUNCTION----------------------------------------->
def difference(mx_cap,ppl):

    
    diff = mx_cap-ppl

    return diff

#gather necessary data of people attending and max cap in room.
    meeting_name = str(input(f"Enter meeting name: "))
    mx_cap = int(input(f"How many people are in the room? "))
    people_attend =int(input(f"How many people are attending? "))
#pass values to call fucntion 
    diff = difference(mx_cap, people_attend)
#display answer 
    print(diff)
#------------------------FUNCTION------------------------------------------------->
def decision(response,continue_resp):

    response = str(input(f"\tWould you like to enter another meeting room? [y/n]: "))
    
    return response
#gather necessary data of people attending and max cap in room.
    response = str(input(f"\tWould you like to enter another meeting room? [y/n]: "))
    continue_resp = str(input(f"\tWould you like to continue in program? [y/n]: ")) 
#pass value to call function
    answer = decision(response,continue_resp)
#display answer
    print(answer)
#-------------------------MAIN CODE------------------------------------------------->
print("Welcome to Meeting Room Fire Regulations Program")

meeting_name = str(input(f"Enter meeting name: "))
mx_cap = int(input(f"How many people are in the room? "))
people_attend =int(input(f"How many people are attending? "))

#initialize variables
count_mx_cap = 0
count_people_attend = 0
diff = mx_cap - people_attend

print(diff)

answer = "y"

while difference == "y" and difference == "N":
    #pass value to function
    diff = difference(mx_cap, people_attend)
    #user inputs
    meeting_name = str(input(f"Enter meeting name: "))
    mx_cap = int(input(f"How many people are in the room? "))
    people_attend =int(input(f"How many people are attending? "))
    
    diff_mx_cap += mx_cap
    diff_people_attend += people_attend
    
if mx_cap < people_attend:
        print(f"The number {diff:.1f} does not meet safety regulations is ILLEGAL!, remove {diff:.1f} people from meeting room. ")
elif mx_cap > people_attend: 
        print(f"The number {diff:.1f}  meets safety regulations and is LEGAL!, add {diff:.1f} to meeeting room. ")

while decision == "y" and decision == "N":
    answer = decision(response,continue_resp)

    response = str(input(f"\tWould you like to enter another meeting room? [y/n]: "))
    continue_resp = str(input(f"\tWould you like to continue in program? [y/n]: ")) 
    
    decision_response += response
    decision_continue_resp += continue_resp
    
    print(answer)
else:
    print("\nGoodbye!")
   

    
    





