# main.py (or wherever your main application loop is)
from calculator.invoker import Invoker

def main():
    invoker = Invoker()
    
    # Example REPL loop
    while True:
        user_input = input("Enter command (or 'menu' to list commands): ").strip()
        if user_input == "exit":
            break
        if user_input == "menu":
            invoker.show_menu()
            continue

        command_name, *args = user_input.split()
        try:
            result = invoker.execute(command_name, *args)
            print(f"Result: {result}")
        except ValueError as err:
            print(err)

if __name__ == "__main__":
    main()
