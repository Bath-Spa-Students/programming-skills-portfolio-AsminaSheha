#Write a Python program to merge two dictionaries into one.

# Sample dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Merge dictionaries using update()
merged_dict = dict1.copy()  
merged_dict.update(dict2)

# Print the merged dictionary
print("Merged Dictionary using update():", merged_dict)
