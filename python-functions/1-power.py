# Function to compute a to the power of b and return the value
def pow(a, b):
    return a ** b
#!/usr/bin/env python3
pow = __import__('1-power').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))