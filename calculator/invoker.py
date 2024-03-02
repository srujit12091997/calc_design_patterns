# invoker.py
from decimal import Decimal
from .operations import add, subtract, multiply, divide, operation_names
from .command import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class Invoker:
    def __init__(self):
        self._commands = {}

    def register(self, command_name: str, a: Decimal, b: Decimal):
        if command_name == "add":
            self._commands[command_name] = AddCommand(a, b)
        elif command_name == "subtract":
            self._commands[command_name] = SubtractCommand(a, b)
        elif command_name == "multiply":
            self._commands[command_name] = MultiplyCommand(a, b)
        elif command_name == "divide":
            self._commands[command_name] = DivideCommand(a, b)

    def execute(self, command_name: str):
        if command_name in self._commands:
            return self._commands[command_name].execute()
        else:
            raise ValueError(f"Command [{command_name}] not recognized")

    def show_menu(self):
        print("Available commands:")
        for command in operation_names:
            print(f"- {command}: {operation_names[command]}")
