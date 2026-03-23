import sqlite3
from datetime import datetime

def log_request(endpoint, method, status):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            endpoint TEXT,
            method TEXT,
            status INTEGER,
            timestamp TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO logs (endpoint, method, status, timestamp)
        VALUES (?, ?, ?, ?)
    """, (endpoint, method, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()
