from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from fastapi_users_db_mongodb import MongoDBUserDatabase
from fastapi_users import FastAPIUsers
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from motor.motor_asyncio import AsyncIOMotorClient
import os
from contextlib import asynccontextmanager
from api.routers import plant_router, soil_router, weather_router
from api.user.routers import get_users_router
from api.routers.limiter import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from api.config import settings
from api.user.auth import jwt_authentication
from api.user.models import ID, User, UserCreate, UserUpdate, UserDB
import uvicorn


# Database Configurations
uri = os.getenv('DB_URL')
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    raise Exception("The following error occurred: ", e)
finally:
    client.close()

app = FastAPI()

async def cancellation_dependency(request: Request = Depends()):
    try:
        yield
    except HTTPException as exc:
        request.abort()
        raise exc

app.dependency_overrides[cancellation_dependency] = cancellation_dependency

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL, uuidRepresentation="standard")
    app.db = app.mongodb_client.get_default_database()

    user_db = MongoDBUserDatabase(UserDB, app.db["users"])

    app.fastapi_users = FastAPIUsers(
        user_db,
        [jwt_authentication],
        ID,
        User,
        UserCreate,
        UserUpdate,
        UserDB,
    )

    app.include_router(plant_router(app), prefix="/plant", tags=["plant"])
    app.include_router(soil_router(app), prefix="/soil", tags=["soil"])
    app.include_router(weather_router(app), prefix="/weather", tags=["weather"])
    app.include_router(get_users_router(app), prefix="/users", tags=["users"])

    yield

    # Shutdown event
    app.mongodb_client.close()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

allow_all = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all
)

@app.get("/")
def read_root():
    return Response("Server is running.")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
        lifespan="lifespan",
    )
