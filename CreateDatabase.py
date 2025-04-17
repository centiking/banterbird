import sqlite3
import os

# Make sure the folder exists
os.makedirs('database', exist_ok=True)

# Connect and create table
conn = sqlite3.connect('database/database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
''')

conn.commit()
conn.close()
print("Database and table created.")
