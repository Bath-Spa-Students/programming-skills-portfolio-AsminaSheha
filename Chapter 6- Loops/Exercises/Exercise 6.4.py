# Create a list of sandwich orders
sandwich_orders = ["roast beef", "ham", "chicken", "pastrami", "veggie"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Process each sandwich order
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Get the first order in the list
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Print the list of finished sandwiches
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
