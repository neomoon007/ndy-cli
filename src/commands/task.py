# Tasks module, add, complete and remove tasks from the 'tasks' database
from .. import database as db

def add(name, date_input=0): # Reacts to the `add` command
    # Insert a task with the name given into the DB
    db.cursor.execute("INSERT INTO tasks (name, done) VALUES (?, ?)", (name, False))
    
    # Save the changes
    db.conn.commit()

    # Close the DB connection
    db.cursor.close()
    db.conn.close()


def edit(name): # Reacts to the `edit` command
    # WIP


def complete(name): # Reacts to the `comp` command
    # WIP


def delete(name): # Reacts to the `del` command
    # WIP


def query(name): # Reacts to the `list` command
    # WIP
