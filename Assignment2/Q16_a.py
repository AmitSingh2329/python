import math

# Get user input
n = int(input("Enter the number of terms (n) for series a): "))
x = float(input("Enter the value of x: "))

# Calculate the sum of the series
sum_a = 0
for i in range(n + 1):
    term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    sum_a += term

print(f"The sum of the series a for n={n} and x={x} is: {sum_a}")

