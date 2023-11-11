#Write a Python function that calculates the factorial of a given positive integer using recursion.

def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n - 1)

# Example usage
number = 179
result = factorial(number)
print(f"The factorial of {number} is:", result)
