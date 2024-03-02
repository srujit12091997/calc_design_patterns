# app/plugins/divide.py
from calculator.commands.command import Command
from calculator.operations import divide
from decimal import Decimal

class DivideCommand(Command):
    def __init__(self, a, b):
        self.a = Decimal(a)
        self.b = Decimal(b)

    def execute(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return divide(self.a, self.b)
