from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

users = {}

class signup_info(BaseModel):
    username: str
    email: str
    password: str

@app.post("/signup")
async def sign_up(info: signup_info):
    signup_info.username = len(users) + 1
    users[signup_info.username] = users
    return HTMLResponse(content="<h1>Successful sign up!</h1>", status_code=200)

@app.get("/")
async def index():
    with open("./signup.html") as file:
        content = file.read()
    return HTMLResponse(content=content)