# To-Do List CLI
from src.interface import menu
from src.utils import dblink


# Create a function that initiates the program
def main():

    # Creates the database table (only if it doesn't exist already)
    dblink.c.execute("""CREATE TABLE IF NOT EXISTS tasks 
            (id INTEGER PRIMARY KEY, name text, done BOOLEAN)""")

    while True:
        if menu.show_menu() == "quit":
            dblink.c.close() # Closes the cursor object
            dblink.conn.close() # Closes the database connection
            break


if __name__ == "__main__":
    main()
