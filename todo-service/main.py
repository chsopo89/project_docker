from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Todo(BaseModel):
    title: str


todos = [
    {"id": 1, "title": "FastAPI 공부하기"},
    {"id": 2, "title": "Docker 공부하기"}
]


@app.get("/")
def hello():
    return {"message": "Hello Todo Service"}


@app.get("/todos")
def get_todos():
    return todos


@app.post("/todos")
def create_todo(todo: Todo):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title
    }

    todos.append(new_todo)

    return new_todo