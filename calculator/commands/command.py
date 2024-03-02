# command.py
from abc import ABC, abstractmethod
from typing import Any
from decimal import Decimal
from calculator.commands.calculations import Calculations
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide


class Command(ABC):
    @abstractmethod
    def execute(self) -> Any:
        pass


class AddCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation.create(a, b, add)

    def execute(self) -> Decimal:
        result = self.calculation.perform()
        Calculations.record_calculation(self.calculation)
        return result


class SubtractCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation.create(a, b, subtract)

    def execute(self) -> Decimal:
        result = self.calculation.perform()
        Calculations.record_calculation(self.calculation)
        return result


class MultiplyCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation.create(a, b, multiply)

    def execute(self) -> Decimal:
        result = self.calculation.perform()
        Calculations.record_calculation(self.calculation)
        return result


class DivideCommand(Command):
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation.create(a, b, divide)

    def execute(self) -> Decimal:
        if self.calculation.b == Decimal('0'):
            raise ValueError("Cannot divide by zero")
        result = self.calculation.perform()
        Calculations.record_calculation(self.calculation)
        return result
