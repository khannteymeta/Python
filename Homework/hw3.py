# Using while loop for write calculation

while True:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operation (+, -, *, /): ")

    match operator:
        case "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        case "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        case "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        case "/":
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
        case _:
            print("Invalid operator! Please try again.")

    # Ask if user wants to continue
    choice = input("Do you want to calculate again? (yes/no): ").lower()
    if choice != "yes":
        print("Calculator closed. Goodbye!")
        break
