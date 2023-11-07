'''Write a python program that takes an input 5 from user and then type cast those values to string, int
and float in the separate variables. Print all the variables.'''

# Take 5 inputs from the user
input_values = []
for i in range(5):
    user_input = input(f"Enter value {i + 1}: ")
    input_values.append(user_input)

# Type cast the input values to string, int, and float
string_values = input_values.copy()  # Cast to string
int_values = [int(value) for value in input_values]  # Cast to int
float_values = [float(value) for value in input_values]  # Cast to float

# Print the variables
print("String values:", string_values)
print("Integer values:", int_values)
print("Float values:", float_values)
