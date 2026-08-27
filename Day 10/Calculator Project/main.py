# Calculator Project
import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(num_1,operation, num_2):
    if mathematical_operation == "+":
        return calculator_operations["+"](num_1, num_2)
    elif mathematical_operation == "-":
        return calculator_operations["-"](num_1, num_2)
    elif mathematical_operation == "*":
        return calculator_operations["*"](num_1, num_2)
    elif mathematical_operation == "/":
        return calculator_operations["/"](num_1, num_2)
    else:
        return "Invalid operation"

calculator_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(art.logo)

first_number = int(input("Enter first number: "))
mathematical_operation = input("Enter mathematical operation \n + \n - \n * \n / \n : ")
second_number = int(input("Enter second number: "))

print(calculate(first_number, mathematical_operation, second_number))
