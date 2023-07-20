# Function to reverse a string
def reverse_string(string):
    # Using slicing to reverse the string
    reversed_string = string[::-1]
    return reversed_string

#!/usr/bin/env python3
reverse_string = __import__('3-string').reverse_string

print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))