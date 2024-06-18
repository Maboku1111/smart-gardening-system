from fastapi import APIRouter, Request
from ..models import User
from .limiter import limiter


router = APIRouter(
    prefix="/users",
)


# User Management
@router.post("/users", response_model = User)
@limiter.limit("1/second")
async def create_new_user(request: Request, user: User):
    return user

@router.get("/users", response_model = User)
@limiter.limit("1/second")
async def get_all_users(request: Request, user: User):
    return user

@router.get("/users/{user_id}", response_model = User)
@limiter.limit("1/second")
async def get_single_user_by_id(request: Request, user_id: int):
    return user_id

@router.patch("/users/{user_id}", response_model = User)
@limiter.limit("1/second")
async def update_user_profile(request: Request, user_id: int):
    return user_id

@router.delete("/users/{user_id}")
@limiter.limit("1/second")
async def delete_item(request: Request, user_id: int):
    return {f"message": "{user_id} deleted successfully"}