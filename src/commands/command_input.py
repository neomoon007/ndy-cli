# This module formats the string input from the user prompt

from termcolor import colored

from . import task

# Example input string: "add 'walk the dog' on monday"
# Example output: calls task.add("walk the dog", "monday")

# Create a funtion that formats the 'user_input' string
def input_handler(string):
    # Check if the string is empty
    if string == "":
        print(colored("ERROR: Please give a valid command.", "red"))
        return 

    # Check if the input is to exit the program
    if string.strip() == "quit":
        return "quit"

    # Split the sentence in a list of words
    words = string.split() 

    # Create a list with the valid commands
    commands = ["add", "edit", "del", "comp", "list"]
    # Check if the command passed is not valid
    if words[0] not in commands:
        print(colored("ERROR: Please give a valid command.", "red"))

    # Check if the command has no arguments
    if len(words) == 1:
        print(colored("ERROR: No arguments passed.", "red"))
        return
    
    # Command input from the user
    command = words[0]
    # Stores the arguments
    arguments = [] 
    # Store current_argument being processed
    current_argument = ""
    # Eliminate the "on" word
    delete_word = False
    # Create a list of words to ignore from the input
    exclude_words = ["on","to","at"]


    # For loop that processes the arguments inside the words list
    for word in words[1:]:
        # If a word starts with ' and there's no argument being processed
        if word.startswith("'") and not current_argument:
            # It stores that word in the current_argument variable
            current_argument = word
        # If however, there's an argument being processed:
        elif current_argument:
            # It adds the word to the current argument, making it bigger
            current_argument += " " + word
            # And if it ends with ':
            if word.endswith("'"):
                # It adds the current_argument to the arguments list
                arguments.append(current_argument.strip("'"))
                # And finishes processing the current argument
                current_argument = ""
                # Allow to delete the next words if in exclude_words list
                delete_word = True
        else:
            # If not allowed to delete word, append it to arguments
            if delete_word == False:
                arguments.append(word)
            # If word is not a word that can be excluded, add it to arguments
            elif word not in exclude_words:
                arguments.append(word)
   
    # Calls the function based on the command given by the user
    if command == "add":
        task.add(*arguments)
    elif command == "edit":
        task.edit(*arguments)
    elif command == "del":
        task.delete(*arguments)
    elif command == "comp":
        task.complete(*arguments)
    elif command == "list":
        task.list(*arguments)
