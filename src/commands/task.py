# Tasks module, add, complete and remove tasks from the 'tasks' database
from . . utils import dblink

def add(name):
    # Insert a task with the name given into the DB
    dblink.c.execute("INSERT INTO tasks (name, done) VALUES (?, ?)", (name, False))
    
    # Save the changes
    dblink.conn.commit()

    # Close the DB connection
    dblink.c.close()
    dblink.conn.close()
