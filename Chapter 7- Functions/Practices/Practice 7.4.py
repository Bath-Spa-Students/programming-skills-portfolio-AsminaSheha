'''Write a Python program that defines a function to calculate the area of a circle, and then calls that 
function with a given radius.'''

import math

def calculate_circle_area(radius):
    return math.pi * radius**2

# Example usage
radius = 20
print(f"The area of a circle with radius {radius} is: {calculate_circle_area(radius):.2f}")
