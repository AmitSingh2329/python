input_string = input("Please enter a string: ")

for start in range(len(input_string)):
    substring = ""
    for end in range(start, len(input_string)):
        substring += input_string[end]
        print(substring)
