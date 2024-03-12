# app/__init__.py

import os
import importlib
import sys
import logging.config
from app.commands import CommandHandler

class App:
    def __init__(self):
        # Set up logging and other initial configurations
        self.setup_logging()
        self.command_handler = CommandHandler()
        self.load_plugins()

    def setup_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def load_plugins(self):
        # The directory where plugins are located
        plugins_dir = os.path.join(os.path.dirname(__file__), 'plugins')
        for item in os.listdir(plugins_dir):
            if os.path.isdir(os.path.join(plugins_dir, item)):
                plugin_name = item
                try:
                    plugin_module = importlib.import_module(f'.plugins.{plugin_name}', 'app')
                    command_class_name = plugin_name.capitalize() + 'Command'
                    command_class = getattr(plugin_module, command_class_name)
                    self.command_handler.register_command(plugin_name, command_class())
                    logging.info(f"Command '{plugin_name}' registered.")
                except (ImportError, AttributeError) as e:
                    logging.error(f"Failed to load plugin '{plugin_name}': {e}")

    def run(self):
        logging.info("Application started. Type 'exit' to quit.")
        while True:
            try:
                command_input = input('>>> ').strip()
                if command_input.lower() == 'exit':
                    logging.info("Application exiting.")
                    break
                self.command_handler.execute_command(command_input)
            except Exception as e:
                logging.error(f"An error occurred: {e}")

if __name__ == '__main__':
    app = App()
    app.run()
