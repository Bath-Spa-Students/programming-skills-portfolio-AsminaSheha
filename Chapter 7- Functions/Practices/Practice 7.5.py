#Write a Python program that defines a function to check whether a given number is prime

def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))

# Example usage
num_to_check = 780

print(f"{num_to_check} is {'a prime' if is_prime(num_to_check) else 'not a prime'} number.")
