import motor.motor_asyncio
from beanie import Document
from fastapi_users.db import BeanieBaseUser
from fastapi_users_db_beanie import BeanieUserDatabase
import os
from .config import settings

DATABASE_URL = os.getenv("DATABASE_URL")
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client[settings.DB_NAME]


class User(BeanieBaseUser, Document):
    pass


async def get_user_db():
    yield BeanieUserDatabase(User)