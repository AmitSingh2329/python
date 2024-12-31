# Get user input
n = input("Enter a positive integer: ")

# Check if the input is a positive integer
if n.isdigit():
    # Initialize an empty string for the reversed number
    reversed_n = ''
    
    # Loop through the digits in reverse order
    for digit in n:
        reversed_n = digit + reversed_n  # Prepend each digit to reverse
    
    print(f"The reversed number is: {reversed_n}")
else:
    print("Please enter a valid positive integer.")
