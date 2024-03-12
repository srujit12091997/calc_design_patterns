import logging
from app.commands import Command

class DivideCommand(Command):
    def execute(self, *args, **kwargs):
        if len(args) < 2:
            raise ValueError("Division requires at least two numbers.")
        if 0 in args[1:]:
            raise ValueError("Cannot divide by zero.")
        result = args[0]
        for arg in args[1:]:
            result /= arg
        logging.info(f"Division result: {result}")
        print(f"Result: {result}")
