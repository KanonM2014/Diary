from fastapi import APIRouter
Router = APIRouter()

@Router.post("/login")
def login(username, password):
    file=open("login.txt","a+")
    file.seek(0)
    login_var=file.read()
    login_var=login_var.split("\n")

    or_username=login_var[0]
    or_username=or_username.split("=")
    or_username=or_username[1]
    or_password=login_var[1]
    or_password=or_password.split("=")
    or_password=or_password[1]


    if username == or_username and password == or_password:
        return "Login successful"
    else:
        return "Login failed"