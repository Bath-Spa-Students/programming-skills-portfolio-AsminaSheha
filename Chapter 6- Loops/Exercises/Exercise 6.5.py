# Create a list of sandwich orders
sandwich_orders = ["pastrami", "roast beef", "ham", "pastrami", "chicken", "pastrami", "veggie"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Print a message that the deli has run out of pastrami
print("Sorry, the deli has run out of pastrami sandwiches.")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process each remaining sandwich order
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Get the first order in the list
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
