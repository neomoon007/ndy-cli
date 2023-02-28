# Configuration file for the program
from termcolor import colored

prompt_style = "Prompt " + colored(">> ", "green")

def prompt():
    user_input = input(prompt_style)
    return user_input
