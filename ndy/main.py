# To-Do List CLI
from src.interface import menu
from src.commands.command_input import input_handler
from src.config import prompt


# Create a function that initiates the program
def main():
    # Display the menu
    menu.show_menu()

    # Create the infinite loop that keeps the program running
    while True:
        # Store the command given in the user_input variable
        user_input = input_handler(prompt())
        # If the input is quit, it exits the program
        if user_input == "quit":
            break


if __name__ == "__main__":
    main()
