import sqlite3
conn = sqlite3.connect('ma_base.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     age INTERGER
)
""")

conn.commit()