def factorial(n):
  # If n is 0 or 1, the factorial is 1.
  if n == 0 or n == 1:
      return 1
    
  else:
      return n * factorial(n - 1)

# Example usage:
n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}")
