# Tasks module, add, complete and remove tasks from the 'tasks' database
from .. import database as db

def add(name, date_input=0):
    # Insert a task with the name given into the DB
    # db.cursor.execute("INSERT INTO tasks (name, done) VALUES (?, ?)", (name, False))
    
    # Save the changes
    # db.conn.commit()

    # Close the DB connection
    # db.cursor.close()
    # db.conn.close()

    # Debug
    print("add()")
    input("wait... ")


def edit(name):
    print("edit()")
    input("wait... ")


def complete(name):
    print("complete()")
    input("wait... ")


def delete(name):
    print("delete()")
    input("wait... ")



