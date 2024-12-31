number = int(input("Enter a positive integer: "))
            
sum_of_primes = 0

for num in range(2, number):
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
        
    if is_prime:
        sum_of_primes += num

print(f"The sum of all prime numbers below {number} is {sum_of_primes}.")
