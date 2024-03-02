# app/plugins/add.py
from calculator.commands.command import Command
from calculator.operations import add
from decimal import Decimal

class AddCommand(Command):
    def __init__(self, a, b):
        self.a = Decimal(a)
        self.b = Decimal(b)

    def execute(self):
        return add(self.a, self.b)
