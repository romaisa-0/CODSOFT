def add(x, y):
    """Perform addition."""
    return x + y

def subtract(x, y):
    """Perform subtraction."""
    return x - y

def multiply(x, y):
    """Perform multiplication."""
    return x * y

def divide(x, y):
    """Perform division."""
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def get_user_input():
    """Get valid numeric input from the user."""
    while True:
        try:
            num = float(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_user_operation():
    """Get valid operation choice from the user."""
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            return choice
        else:
            print("Invalid input. Please enter a valid choice (1/2/3/4).")

def calculator():
    """Main calculator function."""
    print("Welcome to the Professional Calculator!")

    num1 = get_user_input()
    num2 = get_user_input()

    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = get_user_operation()

    if choice == '1':
        result = add(num1, num2)
        operation = 'Addition'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = 'Subtraction'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = 'Multiplication'
    elif choice == '4':
        result = divide(num1, num2)
        operation = 'Division'

    print(f"\n{operation} result: {result}")

if __name__ == "__main__":
    calculator()
