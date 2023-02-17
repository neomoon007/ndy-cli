# To-Do List CLI
from src.interface import menu


# Create a function that initiates the program
def main():
    while True:
        if menu.show_menu() == "quit":
            break


if __name__ == "__main__":
    main()
