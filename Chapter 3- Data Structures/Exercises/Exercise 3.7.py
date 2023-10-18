# Create a list of places to visit
places_to_visit = ["Athirappilli waterfalls", "Kodaikanal", "Munnar", "Palakkad", "Silver Storm"]

# Print the original list
print("Original list:")
print(places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the original list
print("\nSorted list (alphabetical order):")
print(sorted(places_to_visit))

# Show that the original list is still in its original order
print("\nOriginal list (still in original order):")
print(places_to_visit)

# Use sorted() to print the list in reverse alphabetical order without changing the original order
print("\nSorted list (reverse alphabetical order):")
print(sorted(places_to_visit, reverse=True))

# Show that the original list is still in its original order
print("\nOriginal list (still in original order):")
print(places_to_visit)

# Use reverse() to change the order of the list
places_to_visit.reverse()
print("\nReversed list:")
print(places_to_visit)

# Use reverse() again to change the order back to the original order
places_to_visit.reverse()
print("\nReversed list (back to original order):")
print(places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("\nList sorted in alphabetical order:")
print(places_to_visit)

# Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("\nList sorted in reverse alphabetical order:")
print(places_to_visit)

