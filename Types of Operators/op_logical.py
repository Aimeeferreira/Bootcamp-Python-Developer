'''
AND = To be True, everything must be True.
OR = To be True, at least one must be True.

Following from left to right.
'''

# Simple usage examples:

print(True and True)
print(True and False)
print(False and False)
print(True  and False and True)
print(False and False)

print(True  or True)
print(True  or False)
print(True  or True or True)
print(True  or False)
print(False or False)

balance = 1000
withdrawal = 250
limit = 200
special_account = True

ex = balance >= withdrawal and withdrawal <= limit or special_account and balance >= withdrawal
print(ex)

ex_2 = (balance >= withdrawal and withdrawal <= limit) or (special_account and balance >= withdrawal)
print(ex_2)

regular_account_with_sufficient_balance   = balance >= withdrawal and withdrawal <= limit
special_account_with_sufficient_balance = special_account and balance >= withdrawal

ex_3 = regular_account_with_sufficient_balance or special_account_with_sufficient_balance
print(ex_3)
