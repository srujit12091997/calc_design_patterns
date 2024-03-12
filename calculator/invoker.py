# invoker.py
import os  # Import the os module
from decimal import Decimal, InvalidOperation
from calculator.plugin_loader import load_plugins

class Invoker:
    def __init__(self, plugins_path=None):
        if plugins_path is None:
            # Use a default path for plugins if none is provided
            plugins_path = os.path.join(os.path.dirname(__file__), "plugins")
        # Load commands from the specified plugins directory
        self._commands = load_plugins(plugins_path)

    def execute(self, command_name: str, *args):
        try:
            # Convert string arguments to Decimal
            decimal_args = [Decimal(arg) for arg in args]
        except InvalidOperation:
            # Raise an error if input is not numerical
            raise ValueError("Invalid input. Only numerical values are accepted.")

        command_class = self._commands.get(command_name)
        if command_class:
            # Instantiate and execute the command if registered
            if len(decimal_args) != 2:
                raise ValueError(f"Command '{command_name}' expects exactly two numerical arguments.")
            command_instance = command_class(*decimal_args)
            return command_instance.execute()
        else:
            # If the command is not found, raise a ValueError
            raise ValueError(f"No command with name '{command_name}' registered.")

    def show_menu(self):
        # Print out the available commands
        print("Available commands:")
        for command in self._commands.keys():
            print(f"- {command}")

    def is_command_registered(self, command_name):
        # Check if the specified command is registered
        return command_name in self._commands
