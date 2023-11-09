# Get the month as input
month = input("Enter the month (1-12): ")

# Convert the input to an integer
month = int(month)

# Check the season based on the month
if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Fall")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("Invalid month. Please enter a month between 1 and 12.")
