import sqlite3
from contextlib import contextmanager

@contextmanager

def get_connection():
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
    try:
        yield conn
    finally:
        conn.commit()
        conn.close()    