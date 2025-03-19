# Examples of conditions with if | else | elif

normal_account = False
university_account = False
special_account = True

balance = 2000  
withdrawal = 1500  
overdraft = 450  

if normal_account:  

    if balance >= withdrawal:  
        print("Withdrawal successful!")  
    elif withdrawal <= (balance + overdraft):  
        print("Withdrawal made using overdraft!")  
    else:  
        print("Unable to complete withdrawal, insufficient funds!")  

elif university_account:  

    if balance >= withdrawal:  
        print("Withdrawal successful!")  
    else:  
        print("Insufficient funds!")  

elif special_account:  
    print("Special account selected!")  

else:  
    print("The system did not recognize your account type, please contact your manager.") 
