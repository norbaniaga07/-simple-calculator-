# Simple Calculator Program

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


# Main Program
print("=== Simple Calculator ===")

# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Choose operation
print("\nChoose operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

# Perform calculation
if choice == '1':
    print("Result:", add(num1, num2))

elif choice == '2':
    print("Result:", subtract(num1, num2))

elif choice == '3':
    print("Result:", multiply(num1, num2))

elif choice == '4':
    print("Result:", divide(num1, num2))

else:
    print("Invalid choice")