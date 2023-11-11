'''Write a Python program that uses a while loop to find the largest number among a series of
user-input values until they enter '0' to exit the loop.'''

# Initialize variables
largest_number = float('-inf')  

# Use a while loop to get user input and find the largest number
while True:
    user_input = input("Enter a number (enter '0' to exit): ")

    # Check if the user wants to exit
    if user_input == '0':
        break

    # Convert user input to a float
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Check if the current number is larger than the current largest_number
    if number > largest_number:
        largest_number = number

# Print the largest number
print("The largest number entered is:", largest_number)
