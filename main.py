# main.py
import sys
from decimal import Decimal, InvalidOperation
from calculator.operations import add, subtract, multiply, divide, operation_names
from calculator.calculations import Calculations
from calculator.invoker import Invoker

def parse_input(command_name, numbers):
    try:
        return [Decimal(num) for num in numbers]
    except InvalidOperation:
        raise ValueError("Invalid number format.")

def main():
    invoker = Invoker()

    while True:
        print("Type 'menu' for commands or 'exit' to quit: ")
        user_input = input().strip().lower()

        if user_input == 'exit':
            sys.exit()
        elif user_input == 'menu':
            invoker.show_menu()
            continue

        command_name = user_input
        if command_name in operation_names:
            numbers = input(f"Enter the numbers to {command_name} separated by spaces: ").split()
            if not numbers:
                print("No numbers provided.")
                continue

            try:
                decimal_numbers = parse_input(command_name, numbers)
                result = decimal_numbers[0]
                for num in decimal_numbers[1:]:
                    invoker.register(command_name, result, num)
                    result = invoker.execute(command_name)

                print(f"The result of {command_name} is: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Unknown command. Please type 'menu' to see available commands.")

if __name__ == "__main__":
    main()
