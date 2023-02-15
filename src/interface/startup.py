# Startup Interface
from termcolor import colored


def format_header(text, color="white", width=60): 
    
    # Make the text argument uppercase
    header_text = text.upper()
    
    # Print the Header
    print(colored("=" * width, color))
    print(colored(header_text.center(width), color))
    print(colored("=" * width, color))

