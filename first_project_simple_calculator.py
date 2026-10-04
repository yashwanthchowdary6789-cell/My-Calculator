# Basic Arithmetic Operations Program
# This program takes two numbers from the user,
# performs arithmetic operations, and handles errors.

try:
    # Take input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    power = num1 ** num2   # Exponentiation (Power)

    # Display results
    print("\n----- Arithmetic Results -----")
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Power:", power)

    # Check for division by zero
    if num2 == 0:
        raise ZeroDivisionError

    # Division
    division = num1 / num2

    # Remainder (Modulus)
    remainder = num1 % num2

    print("Division:", division)
    print("Remainder:", remainder)

# Handle division by zero error
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handle invalid input (non-numeric values)
except ValueError:
    print("Error: Please enter valid numeric values.")

# Handle any other unexpected errors
except Exception as e:
    print("An unexpected error occurred:", e)
