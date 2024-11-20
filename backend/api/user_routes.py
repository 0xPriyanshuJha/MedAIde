from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

user_router = APIRouter()

users_db = {}

class User(BaseModel):
    username: str
    password: str

@user_router.post("/register/")
def register_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = user.password
    return {"success": True, "message": "User registered successfully"}

@user_router.post("/login/")
def login_user(user: User):
    if users_db.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"success": True, "message": "User logged in successfully"}