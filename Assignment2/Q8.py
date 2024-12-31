while True:
    num = int(input("Please enter a positive integer: "))
    if num > 0:
        break

if num % 2 == 0:
    result = num * 2
else:
    result = num ** 2

print("The result is:", result)
