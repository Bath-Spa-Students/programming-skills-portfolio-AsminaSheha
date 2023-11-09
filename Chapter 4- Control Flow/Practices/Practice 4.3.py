'''Write a python program with nested decision structures that perform the following: If amount1
is greater than 10 and amount2 is less than 100, display the greater of amount1 and amount2'''

amount1 = input('Enter amount1:')
amount2 = input('Enter amount2:')

# Convert input values to integers
amount1 = int(amount1)
amount2 = int(amount2)

if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print('amount1 is greater')
    elif amount2 > amount1:
        print('amount2 is greater')
else:
    print('Amounts not in valid range')
