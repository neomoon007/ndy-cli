# Database connection
import sqlite3

conn = sqlite3.connect("data/database.db") # Connects with the database
cursor = conn.cursor() # Creates the cursor object to execute commands


