# calculations.py
from typing import List
from .calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def record_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls.history.append(calculation)

    @classmethod
    def retrieve_history(cls) -> List[Calculation]:
        """Retrieve the entire history of calculations."""
        return cls.history

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def latest_calculation(cls) -> Calculation:
        """Get the latest calculation. Returns None if there's no history."""
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def search_by_operation(cls, operation) -> List[Calculation]:
        """Find and return a list of calculations by operation function."""
        return [calc for calc in cls.history if calc.operation == operation]
