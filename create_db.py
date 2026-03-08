import sqlite3

# database file create karega
conn = sqlite3.connect("database/database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
password TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and users table created successfully")