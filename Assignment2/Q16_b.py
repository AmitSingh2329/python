import math

# Get user input
n = int(input("Enter the number of terms (n) for series b): "))
x = float(input("Enter the value of x: "))

# Calculate the sum of the series
sum_b = 0
for i in range(n + 1):
    term = (x ** i) / math.factorial(i)
    sum_b += term

print(f"The sum of the series b for n={n} and x={x} is: {sum_b}")
