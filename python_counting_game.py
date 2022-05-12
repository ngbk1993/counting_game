import random

print ("######################################################################")
print ("#                     Welcome to counting game                       #")
print ("# Player only can count for minimum 1 count and maximum for 2 counts #")
print ("#                   Whoever reaches 30 first, lose                   #")
print ("######################################################################")

Current_Number = 0
Input_Number   = 0

def Is_Number_Valid (Curr_Num, Nxt_Num):
    #Check if it is more that the current count
    #Check if it is lest that 2 count 
    if (Nxt_Num <= Curr_Num):
        return False
        
    elif (Nxt_Num > Curr_Num + 2):
        return False
        
    else: 
        return True

def Check_Win (Curr_Num):
    if ((Curr_Num + 1) == 30):
        return True
    else:
        return False
        
while(1):

    #Player Turns
    try:
        Input_Number = int(input("Please Key In your Next Number: "))
    except:
        pass
    
    while((Is_Number_Valid(Current_Number, Input_Number)) == False):
            print ("Invalid Number, Please Key in number greater than the current number (" + str(Current_Number) + ")")
            print ("")
            try:
                Input_Number = int(input("Please Key In your Next Number: "))
            except:
                pass
                
    Current_Number = Input_Number
    
    print ("Current Number is :" + str(Current_Number))
    
    if (Check_Win(Current_Number) == True):
        #Check if Current Number is 30
        #Mean Hit 30 already game over
        print ("Player WIN")
        break
        
    #Computer Turns
    #[Todo] Can add a more intelligent Thought here to make player's life harder
    print ("\n\n## Computer's turn ##")   
    Current_Number += random.randint(1,2)  
    print ("## Current Number is :" + str(Current_Number) + "\n\n######################## \n\n")
    
    if (Check_Win(Current_Number) == True):
        print ("Computer WIN")
        #Check if Current Number is 30
        #Mean Hit 30 already game over
        break