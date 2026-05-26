import sqlite3

from fastapi import APIRouter
Router = APIRouter()

@Router.post("/login")
def login(username, password):
    conn = sqlite3.connect('database/diary.db')  
    cursor = conn.cursor()
    cursor.execute ('SELECT username, password FROM login')
    login_var = cursor.fetchone()

    or_username=login_var[0]
    or_password=login_var[1]



    if username == or_username and password == or_password:
        return "Login successful"
    else:
        return "Login failed"