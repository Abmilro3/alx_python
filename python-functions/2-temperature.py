# Function to convert temperature from Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    # Formula to convert Fahrenheit to Celsius: (Fahrenheit - 32) * 5/9
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

#!/usr/bin/env python3
convert_to_celsius = __import__('2-temperature').convert_to_celsius

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))