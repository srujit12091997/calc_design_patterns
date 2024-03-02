# calculation.py
from decimal import Decimal
from typing import Callable

class Calculation:
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a
        self.b = b
        self.operation = operation
    
    @staticmethod
    def create(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> 'Calculation':
        """Factory method to create a new Calculation instance."""
        return Calculation(a, b, operation)

    def perform(self) -> Decimal:
        """Performs the operation with the provided operands and returns the result."""
        return self.operation(self.a, self.b)

    def __repr__(self) -> str:
        """Provides a developer-friendly string representation of the Calculation instance."""
        operation_name = self.operation.__name__ if hasattr(self.operation, '__name__') else 'unknown_operation'
        return f"Calculation({self.a}, {self.b}, {operation_name})"
