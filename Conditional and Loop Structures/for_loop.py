text = input("Enter a text: ")  
VOWELS = "AEIOU"  

# Example using an iterable  
for letter in text:  
    if letter.upper() in VOWELS:  
        print(letter, end="")  
else:  
    print()  # adds a line break  

# Example using the built-in range function  
for number in range(0, 51, 5):  
    print(number, end=" ")
