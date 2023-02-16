# To-Do List CLI
import sqlite3

from src.interface import menu


# Create a function that initiates the program
def main():
    conn = sqlite3.connect("data/database.db") # Connects with the database
    c = conn.cursor() # Creates the cursor object to execute commands
    
    # Creates the database table (only if it doesn't exist already)
    c.execute("""CREATE TABLE IF NOT EXISTS tasks 
            (id INTEGER PRIMARY KEY, name text, done BOOLEAN)""")

    while True:
        if menu.show_menu() == "quit":
            c.close() # Closes the cursor object
            conn.close() # Closes the database connection
            break


if __name__ == "__main__":
    main()
