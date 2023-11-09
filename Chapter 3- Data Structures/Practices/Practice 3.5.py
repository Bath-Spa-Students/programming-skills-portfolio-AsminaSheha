list1 = [5, 10, 15, 20, 25, 50, 20]

# Find the index of the first occurrence of 20
index = -1
for i in range(len(list1)):
    if list1[i] == 20:
        index = i
        break

# If 20 is found, replace it with 200
if index != -1:
    list1[index] = 200

# Print the updated list
print(list1)
