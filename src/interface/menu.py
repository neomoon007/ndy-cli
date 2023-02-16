from termcolor import colored

from . . utils import screen
from . . utils import header
from . . utils.color import color_print, prompt
from . . commands import task


# Create a function that shows the main menu of the application
def show_menu():
    screen.clear()
    header.format("main menu", "blue")
    color_print("(add) - Add a task", "yellow")
    color_print("(end) - Complete a task", "yellow")
    color_print("(del) - Delete a task", "yellow")
    color_print("(list) - List all tasks", "yellow")
    color_print("(quit) - Quit the program", "yellow")
    print("")


    user_input = prompt()

    if user_input == "quit":
        screen.clear()
        return "quit"
