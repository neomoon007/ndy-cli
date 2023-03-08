from termcolor import colored

from . import task

# Example input string: 'add "walk the dog" on monday'
# Example output: calls task.add("walk the dog", "monday")

functions = {
    'add': task.add,
    'edit': task.edit,
    'comp': task.complete,
    'list': task.query,
    'del': task.delete
}
one_line_commands = ['list']


def input_handler(input):
    if input.strip() == "quit":
        return "quit"

    if not is_valid_input(input):
        return

    processed_arguments = process_arguments(input)
    command_input(input, processed_arguments)


def is_valid_input(input):
    # Check if the string is empty
    if input == "":
        print(colored("ERROR: Please give a valid command.", "red"))
        return False

    # Split the sentence in a list of words
    words = input.split()

    # Create a list with the valid commands
    commands = functions

    command_passed = words[0]

    # Check if the command passed is not valid
    if command_passed not in commands:
        print(colored("ERROR: Please give a valid command.", "red"))
        return False

    # Check if the command has no arguments
    if len(words) == 1 and command_passed not in one_line_commands:
        print(colored("ERROR: No arguments passed.", "red"))
        return False

    return True


def process_arguments(input):
    # Stores the arguments
    processed_arguments = []

    # Store current_argument being processed
    current_argument = ""

    ignore_current_word = False
    words_to_ignore = ["on", "to", "at"]  # Ignore 'glue' words
    raw_arguments = input.split()[1:]

    # If there's just one arguments, return it without double quotes
    if len(raw_arguments) == 1:
        processed_arguments.append(raw_arguments[0].strip("\""))
        return processed_arguments

    # Loop that processes the arguments inside the words list
    for argument in raw_arguments:
        # If a word starts with ' and there's no argument being processed
        if argument.startswith("\"") and not current_argument:
            # It stores that word in the current_argument variable
            current_argument = argument

        # If however, there's an argument being processed:
        elif current_argument:
            # It adds the word to the current argument, making it bigger
            current_argument += " " + argument
            # And if it ends with ':
            if argument.endswith("\""):
                # It adds the current_argument to the arguments list
                processed_arguments.append(current_argument.strip("\""))
                # And finishes processing the current argument
                current_argument = ""
                # Allow to delete the next words if in exclude_words list
                ignore_current_word = True
        else:
            # If not allowed to delete word, append it to arguments
            if ignore_current_word is False:
                processed_arguments.append(argument)
            # If word is not a word that can be excluded, add it to arguments
            elif argument not in words_to_ignore:
                processed_arguments.append(argument)

    return processed_arguments


def command_input(input, cmd_arguments):
    command = input.split()[0]

    # Calls the function based on the command given by the user
    for function in functions:
        if command == function:
            functions[function](cmd_arguments)
