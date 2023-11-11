'''Write a Python program that uses the break statement to exit a for loop when a specific
condition is met.'''

# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a for loop to find and print the first even number
for number in numbers:
    if number % 2 == 0:
        print("Found the first even number:", number)
        break
