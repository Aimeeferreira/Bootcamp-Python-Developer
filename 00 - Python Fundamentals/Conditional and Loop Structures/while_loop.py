# While loop example: 

option = -1  

while option != 0:  
    option = int(input("[1] Withdraw \n[2] Statement \n[0] Exit \n: "))  

    if option == 1:  
        print("Withdrawing...")  
    elif option == 2:  
        print("Displaying the statement...")  
else:  
    print("Thank you for using our banking system, see you soon!")
