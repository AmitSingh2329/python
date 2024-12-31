# Initialize a counter to keep track of numbers printed on the current line
count = 0

# Loop through the range from 100 to 1000
for number in range(100, 1001):
    # Check if the number is divisible by 5 or 6
    if number % 5 == 0 or number % 6 == 0:
        # Print the number followed by a space
        print(number, end=' ')
        count += 1
        
        # Check if we have printed 10 numbers in this line
        if count == 10:
            print()  # Print a newline
            count = 0  # Reset the counter
