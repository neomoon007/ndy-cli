from termcolor import colored

def color_print(text="", color="white"):
    print(colored(text, color))


def prompt():
    user_input = input("Prompt " + colored(">> ", "green"))
    return user_input
