# Function to generate the Fibonacci sequence
def fibonacci_sequence(n):
    # Initialize the first two numbers of the sequence
    fib_sequence = [0, 1]

    # Generate the Fibonacci sequence up to the nth number
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence[:n]

#!/usr/bin/env python3
fibonacci_sequence = __import__('4-fibonacci').fibonacci_sequence

print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))