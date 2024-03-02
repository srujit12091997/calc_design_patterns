from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args, **kwargs):
        if command_name in self.commands:
            self.commands[command_name].execute(*args, **kwargs)
        else:
            print(f"No such command: {command_name}")

class PrintCommand(Command):
    def execute(self, *args, **kwargs):
        message = kwargs.get('message', 'No message provided')
        print(f"Message: {message}")
        for arg in args:
            print(f"Additional argument: {arg}")

# Example Usage
if __name__ == "__main__":
    handler = CommandHandler()
    print_command = PrintCommand()
    handler.register_command('print', print_command)

    # Execute the command with positional and keyword arguments
    handler.execute_command('print', "An example argument", message="This is a test message.")
