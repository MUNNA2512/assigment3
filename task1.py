def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test the function
sample_number = 5
print(f"Factorial of {sample_number} is: {factorial(sample_number)}")