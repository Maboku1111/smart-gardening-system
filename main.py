from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import HTTPException
from fastapi_users import FastAPIUsers
from fastapi_users.db import BaseUserDatabase
from contextlib import asynccontextmanager
from api.routers.limiter import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from api.routers import user_router, plant_router, soil_router, weather_router
from api.config import settings
from api.user.schemas import UserCreate, UserUpdate, UserRead
from api.db import db, User
import uvicorn
from beanie import init_beanie
from api.auth import jwt_authentication

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
    await init_beanie(
        database=db,
        document_models=[
            User,
        ],
    )

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

class CustomUserDatabase(BaseUserDatabase[User, UserCreate]):
    async def get(self, id: str) -> User | None:
        return await User.get(id)

    async def get_by_email(self, email: str) -> User | None:
        return await User.find_one(User.email == email)

    async def create(self, user: UserCreate) -> User:
        user = User(**user.dict())
        await user.insert()
        return user

    async def update(self, user: User) -> User:
        await user.save()
        return user

    async def delete(self, user: User) -> None:
        await user.delete()

user_db = CustomUserDatabase()
fastapi_users = FastAPIUsers(
    User,
    [jwt_authentication],
    user_db,
    UserCreate,
    UserUpdate,
    User,
)

app.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)

app.include_router(user_router.router)
app.include_router(plant_router.router)
app.include_router(soil_router.router)
app.include_router(weather_router.router)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(fastapi_users.current_user(active=True))):
    return {"message": f"Hello {user.email}!"}

@app.get("/")
def read_root():
    return Response("Server is running.")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        log_level="info",
        reload=settings.DEBUG_MODE,
        port=settings.PORT,
        lifespan="lifespan",
    )



