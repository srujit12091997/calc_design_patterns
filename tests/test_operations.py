"""
# test_operations.py
'''Testing Operations'''
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_operation_add():
    '''Testing the addition operation'''
    calculation = Calculation(Decimal('10'), Decimal('5'), add)
    assert calculation.perform() == Decimal('15'), "Add operation failed"

def test_operation_subtract():
    '''Testing the subtract operation'''
    calculation = Calculation(Decimal('10'), Decimal('5'), subtract)
    assert calculation.perform() == Decimal('5'), "Subtract operation failed"

def test_operation_multiply():
    '''Testing the multiply operation'''
    calculation = Calculation(Decimal('10'), Decimal('5'), multiply)
    assert calculation.perform() == Decimal('50'), "Multiply operation failed"

def test_operation_divide():
    '''Testing the divide operation'''
    calculation = Calculation(Decimal('10'), Decimal('5'), divide)
    assert calculation.perform() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
"""

import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def operation_test(value1, value2, method, expected_outcome):
    """
    Validates arithmetic operations to ensure accuracy.
    """
    calc_instance = Calculation.initialize(value1, value2, method)
    assert calc_instance.execute() == expected_outcome, f"Error in {method.__name__}"

# The division by zero test remains unchanged, focusing on the specific exception handling.
def check_division_by_zero():
    """
    Confirms that dividing by zero raises a ValueError.
    """
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc_test = Calculation(Decimal('10'), Decimal('0'), divide)
        calc_test.execute()

