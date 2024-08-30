def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = 10  # Change this value to the desired month
print(f"Number of rabbits in month {n}: {fibonacci(n)}")
