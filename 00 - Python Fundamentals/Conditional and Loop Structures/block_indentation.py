# The code will only work if it is properly indented. Example:

def withdraw(amount):
    balance = 500

    if balance >= amount:
        print("Amount withdrawn successfully!")
    
    print("Thank you for being our customer. Have a great day!")

def deposit(amount):
    balance = 500
    balance += amount

withdraw(1000)
