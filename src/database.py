# Database connection
import sqlite3

conn = sqlite3.connect("data/database.db") # Connects with the database
cursor = conn.cursor() # Creates the cursor object to execute commands

cursor.execute("""CREATE TABLE IF NOT EXISTS tasks
                  (id INTEGER PRIMARY KEY, name TEXT, done BOOLEAN)""")
