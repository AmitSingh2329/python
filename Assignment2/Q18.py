# Loop through numbers from 1 to 100
for number in range(1, 101):
    # Check if the number is a multiple of 7
    if number % 7 == 0:
        continue  # Skip this iteration if it's a multiple of 7
    print(number)  # Print the number if it's not a multiple of 7
