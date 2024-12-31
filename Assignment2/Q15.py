# Get user input
number = int(input("Enter a natural number: "))

# Check if the number is a natural number
if number <= 0:
    print("Please enter a natural number greater than 0.")
else:
    # Calculate the sum of divisors
    sum_of_divisors = 0
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors += i

    # Check if the number is a perfect number
    if sum_of_divisors == number:
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")
