from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="사용자 관리 서비스",
    description="사용자를 조회하고 등록하는 API입니다.",
    version="1.0.0"
)


class User(BaseModel):
    name: str


users = [
    {"id": 1, "name": "조병현"},
    {"id": 2, "name": "조형우"},
    {"id": 3, "name": "정준재"}
]


@app.get("/", summary="서버 상태 확인")
def hello():
    return {"message": "사용자 서비스가 정상 작동 중입니다."}


@app.get("/users", summary="사용자 목록 조회")
def get_users():
    return users


@app.post("/users", summary="새 사용자 등록")
def create_user(user: User):
    new_user = {
        "id": len(users) + 1,
        "name": user.name
    }

    users.append(new_user)

    return new_user