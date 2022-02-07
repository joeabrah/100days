from art import logo

# Calculator

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply 
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1/n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# Function for the calculator
def calculator():
    print(logo)

    num1 = float(input("What's the first number?: ")) # Using float instead of integer to make the numbers more accurate

    for symbol in operations:
        print(symbol)

    calc_continue = True
    while calc_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f'Type "yes" to calculate more with {answer} or type "no" to start a new calculation') == 'yes':
            num1 = answer
        else:
            calc_continue = False
            calculator()

calculator()