# Function to check if a number is prime
def is_prime(number):
    # Check if the number is less than 2 (not prime)
    if number < 2:
        return False

    # Check for divisibility from 2 up to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

#!/usr/bin/env python3
is_prime = __import__('5-prime').is_prime

print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))