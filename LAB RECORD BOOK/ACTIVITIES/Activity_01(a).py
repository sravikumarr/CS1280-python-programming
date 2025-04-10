# Simple calculator program to include additional operations: subtraction, multiply, modulus (%), exponentiation (), and floor division (//).
def calculator():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponentiation (**)")
    print("7. Floor Division (//)")
    
    choice = input("Enter choice (1/2/3/4/5/6/7): ")
    
    if choice in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero is not allowed.")
        elif choice == '5':
            print(f"Result: {num1} % {num2} = {num1 % num2}")
        elif choice == '6':
            print(f"Result: {num1} ** {num2} = {num1 ** num2}")
        elif choice == '7':
            if num2 != 0:
                print(f"Result: {num1} // {num2} = {num1 // num2}")
            else:
                print("Error! Division by zero is not allowed.")
    else:
        print("Invalid input. Please enter a valid option.")

# Run the calculator function
calculator()
