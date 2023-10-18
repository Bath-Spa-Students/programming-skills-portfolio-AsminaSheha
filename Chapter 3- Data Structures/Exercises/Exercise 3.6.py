# Invite some people to dinner.
guests = ['Afthab', 'Jahangeer', 'Ajishad' , 'Shahitha']

name = guests[0].title()
print(name + ", It's time you come eat my cooking.Expecting you this Saturday.")

name = guests[1].title()
print(name + ", It's time you come eat my cooking.Expecting you this Saturday.")

name = guests[2].title()
print(name + ", It's time you come eat my cooking.Expecting you this Saturday.")

name = guests[3].title()
print(name + ", It's time you come eat my cooking.Expecting you this Saturday.")

name = guests[3].title()
print("\nSorry, " + name + " can't taste your cooking anytime soon.")

# Shahitha can't make it! Let's invite Shobitha instead.
del(guests[3])
guests.insert(3, 'Shobitha')

# Print the invitations again.
name = guests[0].title()
print("\n" + name + ", It's time you come eat my cooking.Expecting you this Saturday.")

name = guests[1].title()
print(name + ", It's time you come eat my cooking.Expecting you this Saturday.")

name = guests[2].title()
print(name + ", It's time you come eat my cooking.Expecting you this Saturday.")

name = guests[3].title()
print(name + ", It's time you come eat my cooking.Expecting you this Saturday.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

name = guests.pop()
print("Sorry, " + name.title() + " there's no room at the table.")

# There should be two people left. Let's invite them.
name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")
