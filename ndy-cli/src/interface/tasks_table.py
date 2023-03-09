from rich.console import Console
from rich.table import Table
from rich import box


def display_tasks(tasks):
    # Colors
    color1 = "green"
    color2 = "yellow"
    color3 = ""
    color4 = "blue"

    # Columns
    column1 = "ID"
    column2 = "Task"
    column3 = "Done"
    column4 = "Date"

    # Check marks
    uncompleted = "[red]False[/red]"
    completed = "[green]True[/green]"

    console = Console()

    # Create contents table
    content_table = Table(show_header=True,
                          show_edge=True, show_lines=True, box=box.HEAVY_HEAD)

    # Create the columns for the content_table
    content_table.add_column(column1, style=color1)

    content_table.add_column(column2, style=color2, justify="left",
                             max_width=49, no_wrap=True)

    content_table.add_column(column3, style=color3, justify="center",
                             max_width=5, no_wrap=False)

    content_table.add_column(column4, style=color4, justify="left",
                             max_width=20, no_wrap=False)

    # Add rows for the table
    for task in tasks:
        id = str(task[0])
        title = str(task[1])

        # str(task[0])

        if task[2]:
            done = completed
        else:
            done = uncompleted

        # TODO: after creating the date integration, update the line below.
        date = "WIP"

        content_table.add_row(
            id,
            title,
            done,
            date)

    # Print the outline table
    console.print(content_table)
