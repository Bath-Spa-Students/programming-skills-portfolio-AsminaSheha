# Create dictionaries for different pets
pet1 = {'kind': 'Horse', 'owner': 'Sasha'}
pet2 = {'kind': 'Cat', 'owner': 'Mina'}
pet3 = {'kind': 'Fish', 'owner': 'James'}
pet4 = {'kind': 'Parrot', 'owner': 'Drake'}

# Store the dictionaries in a list called 'pets'
pets = [pet1, pet2, pet3, pet4]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Pet kind: {pet['kind']}")
    print(f"Owner's name: {pet['owner']}")
    print()  # Print an empty line to separate pet information
