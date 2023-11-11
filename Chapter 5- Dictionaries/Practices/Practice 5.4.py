'''Write a Python program to iterate through both the keys and values of a dictionary and print
them'''

# Sample dictionary
my_dictionary = {
    "name": "Asmina Shehzadha",
    "age": 19,
    "city": "Dubai",
    "occupation": "Student"
}

# Iterate through both keys and values and print them
print("Keys and Values in the dictionary:")
for key, value in my_dictionary.items():
    print(f"{key}: {value}")