 # Prompt the user for their age as a string

while True:
    age_str = input("Enter your age (or 'quit' to finish): ") 

    if age_str.lower() == 'quit':
        break  # Exit the loop if the user enters 'quit'

# Convert the user's input to an integer
    try:
        age = int(age_str)

# If the age is under 3, the ticket is free  
        if age < 3:
            ticket_price = 0 

# If the age is between 3 and 12 (inclusive), the ticket is $10 
        elif 3 <= age <= 12:
            ticket_price = 10  

# If the age is over 12, the ticket is $15
        else:
            ticket_price = 15  

        print(f"Your movie ticket costs ${ticket_price}")  
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit' to finish.")  

print("Thank you for using the ticketing system!") 
