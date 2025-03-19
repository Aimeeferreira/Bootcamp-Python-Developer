'''
Used to compare whether the two tested objects occupy the same memory location.

Following from left to right.
'''

# Simple usage examples:

balance = 1000
limit = 1000
print(balance is limit)
print(balance is not limit)

balance = 1000
limit = 200
print(balance is limit)
print(balance is not limit)
