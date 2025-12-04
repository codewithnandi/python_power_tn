#declaring and using functions  
def greet(name):
    return "Hello, " + name + "!"
user_name = input("Enter your name: ")
print(greet(user_name))

#factorial calculation using function and recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a non-negative integer to calculate its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}")    

# Fibonacci sequence generation using function
def fibonacci(n): 
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)
    return fib_sequence[:n] 
terms = int(input("Enter the number of terms for Fibonacci sequence: "))
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci sequence with {terms} terms: {fibonacci(terms)}")

# Prime number check using function
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number to check if it's prime: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

