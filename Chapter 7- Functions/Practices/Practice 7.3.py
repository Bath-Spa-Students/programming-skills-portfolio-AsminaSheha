#Write a Python program that uses a function to check if a given number is prime or not

def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))

# Example usage
num_to_check = 20

if is_prime(num_to_check):
    print(f"{num_to_check} is a prime number.")
else:
    print(f"{num_to_check} is not a prime number.")
