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
import uvicorn
from beanie import init_beanie
from api.user.db import User, db
from api.user.schemas import UserCreate, UserRead, UserUpdate
from api.user.users import auth_backend, current_active_user, fastapi_users
# from pymongo import DBRef

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

app = FastAPI(lifespan=lifespan)

async def cancellation_dependency(request: Request = Depends()):
    try:
        yield
    except HTTPException as exc:
        request.abort()
        raise exc

app.dependency_overrides[cancellation_dependency] = cancellation_dependency

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

app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
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
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}

app.include_router(user_router.router)
app.include_router(plant_router.router)
app.include_router(soil_router.router)
app.include_router(weather_router.router)

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
    )



