from fastapi import APIRouter
from app.schemas import UserCreate

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "OK"}

@router.post("/users")
def create_user(user: UserCreate):
    return {"message": f"User {user.name} created"}