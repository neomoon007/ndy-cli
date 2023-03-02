from .. database import conn, cursor
from termcolor import colored


def add(task_title, date_input=0):  # Reacts to the `add` command
    # Insert a task with the name given into the DB
    cursor.execute(
        "INSERT INTO tasks (name, done) VALUES (?, ?)", (task_title, False))

    # Save the changes
    conn.commit()

    print(colored(task_title + "was added successfully.", "green"))


def edit(task_id):
    # TODO: create the task.edit() function
    pass


def complete(task_id):
    num_task_id = int(task_id[0])
    cursor.execute(
        "SELECT done FROM tasks WHERE id=?", (1,)
    )

    task_already_completed = cursor.fetchone()[0]

    # Toggle task 'done' status
    if task_already_completed == 1:
        cursor.execute(
            "UPDATE tasks SET done = ? WHERE id = ?", (False, num_task_id)
        )
        conn.commit()

    elif task_already_completed == 0:
        cursor.execute(
            "UPDATE tasks SET done = ? WHERE id = ?", (True, num_task_id)
        )
        conn.commit()


def delete(task_id):
    # TODO: create the task.delete() function
    pass


def query(filter):
    # TODO: Add filter functionality
    # Get all tasks from the database
    cursor.execute("SELECT * FROM tasks")

    # Fetches all rows from resultset
    tasks = cursor.fetchall()

    # Print the tasks
    for task in tasks:
        print("-" * 60)
        print("ID: " + str(task[0]))
        print("Title: " + str(task[1]))
        print("Done: " + str(task[2]))
        print(" ")
