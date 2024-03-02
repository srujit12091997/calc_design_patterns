# calculator/plugin_loader.py

import os
import importlib.util

def load_plugins(plugin_directory):
    commands = {}
    # Ensure the path is correct, especially if running from a different directory
    plugin_path = os.path.abspath(plugin_directory)
    plugin_files = [f for f in os.listdir(plugin_path) if f.endswith('.py') and not f.startswith('__')]

    for file in plugin_files:
        name = file[:-3]
        try:
            module_spec = importlib.util.spec_from_file_location(name, os.path.join(plugin_path, file))
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            # Construct the class name based on the file name
            command_class_name = name.capitalize() + 'Command'
            if hasattr(module, command_class_name):
                command_class = getattr(module, command_class_name)
                commands[name] = command_class
            else:
                print(f"Warning: Command class '{command_class_name}' not found in '{file}'.")
        except Exception as e:
            print(f"Error loading '{name}': {e}")

    return commands
