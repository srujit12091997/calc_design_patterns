"""
This module contains tests for the Calculation class.
"""

from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_calculation_repr():
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    # Adjust the expected_repr to match the actual implementation
    expected_repr = f"Calculation({Decimal('10')}, {Decimal('5')}, {add.__name__})"
    assert repr(calc) == expected_repr, "The __repr__ method output does not match the expected string."


@pytest.mark.parametrize("a, b, operation, expected", [
    (Decimal('5'), Decimal('3'), add, Decimal('8')),
    (Decimal('10'), Decimal('2'), subtract, Decimal('8')),
    (Decimal('4'), Decimal('5'), multiply, Decimal('20')),
    (Decimal('20'), Decimal('4'), divide, Decimal('5')),
    (Decimal('1'), Decimal('0'), divide, "ZeroDivisionError"),
])
def test_calculation_operations(a, b, operation, expected):
    """Test various calculation operations."""
    if expected == "ZeroDivisionError":
        with pytest.raises(ZeroDivisionError):
            Calculation(a, b, operation).perform()
    else:
        calc = Calculation(a, b, operation)
        assert calc.perform() == expected, f"Expected {expected}, got {calc.perform()}"
        
def test_divide_by_zero():
    """Test division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        Calculation(Decimal('10'), Decimal('0'), divide).perform()
