while True:
    first_input = input("Enter the first number (or type 'exit' to quit): ")
    if first_input.lower() == 'exit':
        print("Exiting the calculator.")
        break
    
    second_input = input("Enter the second number: ")
    
    operator = input("Enter an operator (+, -, *, /): ")
    
    if first_input.replace('.','').isdigit() and second_input.replace('.','').isdigit():
        first_num = float(first_input)
        second_num = float(second_input)
        
        match operator:
            case '+':
                result = first_num + second_num
            case '-':
                result = first_num - second_num
            case '*':
                result = first_num * second_num
            case '/':
                if second_num != 0:
                    result = first_num / second_num
                else:
                    print("Error: Division by zero is not allowed.")
                    continue
            case _:
                print("Invalid operator. Please use +, -, *, or /.")
                continue
        
        print(f"Result: {result}")
    else:
        print("Invalid input. Please enter numeric values for the numbers.")
