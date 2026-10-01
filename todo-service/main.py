from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="할 일 관리 서비스",
    description="할 일을 조회하고 등록하는 API입니다.",
    version="1.0.0"
)


class Todo(BaseModel):
    title: str


todos = [
    {"id": 1, "title": "FastAPI 공부하기"},
    {"id": 2, "title": "Docker 공부하기"}
]


@app.get("/", summary="서버 상태 확인")
def hello():
    return {"message": "할 일 서비스가 정상 작동 중입니다."}


@app.get("/todos", summary="할 일 목록 조회")
def get_todos():
    return todos


@app.post("/todos", summary="새 할 일 등록")
def create_todo(todo: Todo):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title
    }

    todos.append(new_todo)

    return new_todo