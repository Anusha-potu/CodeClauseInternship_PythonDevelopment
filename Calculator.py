def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    choice = input("Enter choice (Add/Sub/Multiply/Div): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 'Add':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 'Sub':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 'Multiply':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 'Div':
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid Input")
calculator()
