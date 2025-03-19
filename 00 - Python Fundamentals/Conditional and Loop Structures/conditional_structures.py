# Examples of if/else conditions  

LEGAL_AGE = 18  
AGE = 17  

age = int(input("Enter your age: "))  

if age >= LEGAL_AGE:  
    print("Of legal age, you can get a driver's license.")  

if age < LEGAL_AGE:  
    print("You cannot get a driver's license yet.")  

if age >= LEGAL_AGE:  
    print("Of legal age, you can get a driver's license.")  
else:  
    print("You cannot get a driver's license yet.")  

if age >= LEGAL_AGE:  
    print("Of legal age, you can get a driver's license.")  
elif age == AGE:  
    print("You can take theoretical lessons, but you cannot take practical lessons.")  
else:  
    print("You cannot get a driver's license yet.")  
    