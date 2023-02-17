# Tasks module, add, complete and remove tasks from the 'tasks' database
from . . utils import database

def add(name):
    # Insert a task with the name given into the DB
    database.cursor.execute("INSERT INTO tasks (name, done) VALUES (?, ?)", (name, False))
    
    # Save the changes
    database.conn.commit()

    # Close the DB connection
    database.cursor.close()
    database.conn.close()
