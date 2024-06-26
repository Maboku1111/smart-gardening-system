from fastapi_users.models import BaseUser, BaseUserCreate, BaseUserUpdate, BaseUserDB

class ID(BaseUser):
    pass


class User(BaseUser):
    pass


class UserCreate(BaseUserCreate):
    pass


class UserUpdate(User, BaseUserUpdate):
    pass


class UserDB(User, BaseUserDB):
    pass