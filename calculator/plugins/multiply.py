# app/plugins/multiply.py
from calculator.commands.command import Command
from calculator.operations import multiply
from decimal import Decimal

class MultiplyCommand(Command):
    def __init__(self, a, b):
        self.a = Decimal(a)
        self.b = Decimal(b)

    def execute(self):
        return multiply(self.a, self.b)
