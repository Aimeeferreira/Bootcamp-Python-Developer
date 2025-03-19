salary = 2000  # Global variable

'''
#invalid

def salary_bonus(bonus):
    salary += bonus  
    return salary

'''

def salary_bonus(bonus, list):
    global salary

    list_aux = list.copy()
    list_aux.append(2)
    print(f"list aux={list_aux}")

    salary += bonus
    return salary

list = [1]
total = salary_bonus(500, list)
print(total)
print(list)

'''
def salary_bonus(bonus, list):
    global salary  
    salary += bonus  
    return salary

list = [1]
total = salary_bonus(500, list)
print(total)
print(list) #1
'''

'''
def salary_bonus(bonus, list):
    global salary  
    list.append(2)
    salary += bonus  
    return salary

list = [1]
total = salary_bonus(500, list)
print(total)
print(list) # [1,2]
'''
