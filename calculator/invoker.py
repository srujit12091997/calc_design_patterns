# Assuming the file path: calculator/invoker.py
from decimal import Decimal, InvalidOperation
from calculator.plugin_loader import load_plugins

class Invoker:
    def __init__(self, plugins_path="calculator/plugins"):
        # Dynamically load commands from the specified plugins directory
        self._commands = load_plugins(plugins_path)

    def execute(self, command_name: str, *args):
        try:
            # Convert string arguments to Decimal, ensuring they are numerical
            decimal_args = [Decimal(arg) for arg in args]
        except InvalidOperation:
            raise ValueError("Invalid input. Only numerical values are accepted.")

        # Retrieve the command class by name
        command_class = self._commands.get(command_name)
        if command_class:
            # Check if the correct number of arguments are provided
            if len(decimal_args) != 2:
                raise ValueError(f"Command '{command_name}' expects exactly two numerical arguments.")
            # Instantiate the command with provided Decimal arguments
            command_instance = command_class(decimal_args[0], decimal_args[1])
            # Execute the command and return the result
            return command_instance.execute()
        else:
            raise ValueError(f"No command with name '{command_name}' registered.")

    def show_menu(self):
        print("Available commands:")
        for command in self._commands.keys():
            print(f"- {command}")
