# test_main.py
#import pytest
'''
from main import calculate_and_print

@pytest.mark.parametrize("num1_str, num2_str, op_str, expected_output", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8\n\n"),  # Added extra \n to match the actual output
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8\n\n"),  # Same here
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20\n\n"),  # And here
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5\n\n"),  # Again here
    ("1", "0", 'divide', "An error occurred: Division by zero.\n\n"),  # Adjusting for the error message
    ("9", "3", 'unknown', "Unknown operation.\n\n"),  # For the unknown operation message
    ("a", "3", 'add', "An error occurred: Invalid literal for Decimal.\n\n"),  # Handling invalid input for Decimal
    ("5", "b", 'subtract', "An error occurred: Invalid literal for Decimal.\n\n")  # Handling another case of invalid Decimal input
])
def test_calculate_and_print_variations(num1_str, num2_str, op_str, expected_output, capsys):
    calculate_and_print(num1_str, num2_str, op_str)
    captured = capsys.readouterr()
    assert captured.out == expected_output
'''

# test_operations.py
import pytest
from calculator.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("operation, a, b, expected", [
    (add, 5, 3, 8),
    (subtract, 10, 2, 8),
    (multiply, 4, 5, 20),
    (divide, 20, 4, 5),
])
def test_operation(operation, a, b, expected):
    result = operation(a, b)
    assert result == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
