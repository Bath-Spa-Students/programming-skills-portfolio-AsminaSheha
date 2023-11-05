while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'
    
    print(f"I'll add {topping} to your pizza.")

print("Your pizza is ready!")
