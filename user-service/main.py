from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str


users = [
    {"id": 1, "name": "조병현"},
    {"id": 2, "name": "조형우"}
]


@app.get("/")
def hello():
    return {"message": "Hello FastAPI"}


@app.get("/users")
def get_users():
    return users


@app.post("/users")
def create_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name
    }

    users.append(new_user)

    return new_user