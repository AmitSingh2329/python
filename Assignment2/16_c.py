# Get user input
n = int(input("Enter the number of terms (n) for series c): "))

# Calculate the sum of the series
sum_c = 0
for i in range(n):
    term = (2 * i + 1) * (-1) ** i  # Odd numbers alternating in sign
    sum_c += term

print(f"The sum of the series c for n={n} is: {sum_c}")
