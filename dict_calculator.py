def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    return a % b

def exponent(a, b):
    return a ** b

def calculator():
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide),
        '5': ('Modulus', modulus),
        '6': ('Exponent', exponent),
    }
    
    while True:
        print("\nMenu:")
        for key, (name, _) in operations.items():
            print(f"{key}: {name}")
        print("0: Exit")
        
        choice = input("Select an operation: ")
        
        if choice == '0':
            print("Exiting the calculator.")
            break
        
        if choice not in operations:
            print("Invalid choice! Please select a valid operation.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
        
        operation_name, operation_function = operations[choice]
        result = operation_function(num1, num2)
        print(f"The result of {operation_name} is: {result}")


calculator()
