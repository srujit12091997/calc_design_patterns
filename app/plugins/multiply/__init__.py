import logging
from app.commands import Command
from functools import reduce
import operator

class MultiplyCommand(Command):
    def execute(self, *args, **kwargs):
        result = reduce(operator.mul, args, 1)
        logging.info(f"Multiplication result: {result}")
        print(f"Result: {result}")
