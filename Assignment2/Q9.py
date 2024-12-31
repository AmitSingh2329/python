user_input = input("Please enter a number: ")

if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
    num = int(user_input)

    match num % 5:
        case 0:
            print("Remainder when divided by 5 is: 0")
        case 1:
            print("Remainder when divided by 5 is: 1")
        case 2:
            print("Remainder when divided by 5 is: 2")
        case 3:
            print("Remainder when divided by 5 is: 3")
        case 4:
            print("Remainder when divided by 5 is: 4")
else:
    print("Invalid input")
