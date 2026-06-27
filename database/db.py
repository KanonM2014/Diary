import sqlite3

def get_connection():
    conn = sqlite3.connect(r"D:\Kanon\Diary\database\Diary.db")
    return conn