from decimal import Decimal

# Add operation names for menu display
operation_names = {
    'add': 'Addition',
    'subtract': 'Subtraction',
    'multiply': 'Multiplication',
    'divide': 'Division'
}

def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
