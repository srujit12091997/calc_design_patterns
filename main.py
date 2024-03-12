# main.py
'''
import sys
import os
from calculator.invoker import Invoker

def main(plugins_path=None):
    # If no specific path to plugins provided, use default
    if plugins_path is None:
        # Default plugins path relative to this script
        base_dir = os.path.dirname(__file__)
        plugins_path = os.path.join(base_dir, 'calculator', 'plugins')
        
    invoker = Invoker(plugins_path=plugins_path)

    print("Calculator is running. Type 'menu' for commands or 'exit' to quit:")
    
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == 'exit':
            print("Exiting the application.")
            sys.exit()
        elif user_input.lower() == 'menu':
            invoker.show_menu()
        else:
            command_name, *args = user_input.split()
            if not invoker.is_command_registered(command_name):
                # Specific handling for unknown commands
                print("Unknown command. Please type 'menu' to see available commands.")
                continue
            
            try:
                result = invoker.execute(command_name, *args)
                print(f"Result: {result}")
            except ZeroDivisionError:
                print("Error: Cannot divide by zero")
            except ValueError as err:
                print(err)
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
'''

# main.py
from app import App    

# You must put this in your main.py because this forces the program to start when you run it from the command line.
if __name__ == "__main__":
    app = App().start()  # Instantiate an instance of App