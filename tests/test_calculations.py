"""Test suite for calculation history management."""

import pytest
from decimal import Decimal
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract

@pytest.fixture
def calculator_setup():
    """Setup fixture for each test."""
    Calculations.clear_history()
    Calculations.record_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.record_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))

def test_record_calculation(calculator_setup):
    """Test recording a new calculation."""
    new_calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.record_calculation(new_calc)
    assert Calculations.latest_calculation() == new_calc, "New calculation was not recorded correctly."

def test_history_retrieval(calculator_setup):
    """Test retrieval of the entire history."""
    assert len(Calculations.retrieve_history()) == 2, "History retrieval failed."

def test_history_reset(calculator_setup):
    """Test resetting the history."""
    Calculations.clear_history()
    assert len(Calculations.retrieve_history()) == 0, "History was not cleared."

def test_latest_calculation_retrieval(calculator_setup):
    """Test retrieval of the latest calculation."""
    assert Calculations.latest_calculation() is not None, "Failed to retrieve the latest calculation."

def test_search_by_operation_type(calculator_setup):
    """Test searching calculations by operation type."""
    adds = Calculations.search_by_operation(add)
    subtracts = Calculations.search_by_operation(subtract)
    assert len(adds) == 1 and len(subtracts) == 1, "Search by operation type failed."

def test_latest_with_no_history():
    """Test that no latest calculation is returned when history is empty."""
    Calculations.clear_history()
    assert Calculations.latest_calculation() is None, "Expected no latest calculation."
