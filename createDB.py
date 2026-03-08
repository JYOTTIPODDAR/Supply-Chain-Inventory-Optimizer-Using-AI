import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users(
    name TEXT,
    email TEXT PRIMARY KEY,
    password TEXT
)
""")

conn.commit()
conn.close()

print("Users table created successfully")