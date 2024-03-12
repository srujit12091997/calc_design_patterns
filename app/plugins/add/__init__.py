import logging
from app.commands import Command

class AddCommand(Command):
    def execute(self, *args, **kwargs):
        result = sum(args)
        logging.info(f"Addition result: {result}")
        print(f"Result: {result}")
