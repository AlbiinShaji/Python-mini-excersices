"""
Simple Calculator
Demonstrates functions and basic input handling.
Supports +, -, *, /
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def calculate(a, operator, b):
    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    if operator not in operations:
        return "Error: Invalid operator"
    return operations[operator](a, b)


if __name__ == "__main__":
    print(calculate(10, "+", 5))   # 15
    print(calculate(10, "-", 5))   # 5
    print(calculate(10, "*", 5))   # 50
    print(calculate(10, "/", 5))   # 2.0
    print(calculate(10, "/", 0))   # Error: Division by zero
