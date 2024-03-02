# app/plugins/subtract.py
from calculator.commands.command import Command
from calculator.operations import subtract
from decimal import Decimal

class SubtractCommand(Command):
    def __init__(self, a, b):
        self.a = Decimal(a)
        self.b = Decimal(b)

    def execute(self):
        return subtract(self.a, self.b)
