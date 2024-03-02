"""Calculation Functionality Tests."""

from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def test_addition():
    """Ensures the add method correctly computes the sum."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    assert calc.perform() == Decimal('4'), "Addition Error"

def test_subtraction():
    """Verifies subtraction accuracy."""
    calc = Calculation(Decimal('2'), Decimal('2'), subtract)
    assert calc.perform() == Decimal('0'), "Subtraction Error"

def test_division():
    """Confirms division method functionality."""
    calc = Calculation(Decimal('2'), Decimal('2'), divide)
    assert calc.perform() == Decimal('1'), "Division Error"

def test_multiplication():
    """Tests multiplication to ensure proper operation."""
    calc = Calculation(Decimal('2'), Decimal('2'), multiply)
    assert calc.perform() == Decimal('4'), "Multiplication Error"
