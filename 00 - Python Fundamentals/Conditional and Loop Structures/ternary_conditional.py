# Example of a condition with a return/response based on the logic of the expression  

balance = 2000  
withdrawal = 2500  

status = "Success" if balance >= withdrawal else "Failure"  

print(f"{status} when making the withdrawal!")  
