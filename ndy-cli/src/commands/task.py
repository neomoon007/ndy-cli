from termcolor import colored

from .. database import conn, cursor


def add(task_title, date_input=0):
    # Insert a task with the name given into the DB

    cursor.execute(
        "INSERT INTO tasks (name, done) VALUES (?, ?)",
        (task_title[0], False))

    # Save the changes
    conn.commit()

    print(colored("\"" + task_title[0] + "\"" +
          " was added successfully.", "green"))


def edit(task_id):
    # TODO: create the task.edit() function
    pass


def complete(task_id):
    num_task_id = int(task_id[0])
    cursor.execute(
        "SELECT done FROM tasks WHERE id=?", (num_task_id,)
    )

    task_already_completed = cursor.fetchone()

    if task_already_completed is None:
        print(colored("ERROR: Invalid task id.", "red"))
        return

    # Toggle task 'done' status
    if task_already_completed[0] == 1:
        cursor.execute(
            "UPDATE tasks SET done = ? WHERE id = ?", (False, num_task_id)
        )
        conn.commit()

    elif task_already_completed[0] == 0:
        cursor.execute(
            "UPDATE tasks SET done = ? WHERE id = ?", (True, num_task_id)
        )
        conn.commit()


def delete(task_id):
    num_task_id = int(task_id[0])
    cursor.execute(
        "SELECT * FROM tasks WHERE id=?", (num_task_id,)
    )

    if cursor.fetchone() is None:
        print(colored("ERROR: Invalid task id.", "red"))

    else:
        cursor.execute(
            "DELETE FROM tasks WHERE id=?", (num_task_id,)
        )
        conn.commit()


def query(filter):
    # Get all tasks from the database

    # TODO: Add filter functionality
    # Filter:
    # Check if the filter == "all": (retrieve all tasks)
    # Check if the filter is a valid human readable date:
    #   (retrieve all tasks that match the given date)
    #
    # Check if the filter is a string: (retrieve tasks that have that string)

    if filter == "all":
        cursor.execute("SELECT * FROM tasks")

    # Fetches all rows from resultset
    tasks = cursor.fetchall()

    # TODO: Use python rich package and format results as a table
    # Print the tasks
    for task in tasks:
        print("-" * 60)
        print("ID: " + str(task[0]))
        print("Title: " + str(task[1]))
        print("Done: " + str(task[2]))
        print(" ")
