import logging
from app.commands import Command

class SubtractCommand(Command):
    def execute(self, *args, **kwargs):
        if len(args) < 2:
            raise ValueError("Subtraction requires at least two numbers.")
        result = args[0] - sum(args[1:])
        logging.info(f"Subtraction result: {result}")
        print(f"Result: {result}")
