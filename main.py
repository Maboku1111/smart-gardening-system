# Entry code for the application
import uvicorn
import pyrebase
import json
from firebase_admin import credentials, auth
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import contextlib
from api.routers.plant_router import router as plant_router
from api.routers.soil_router import router as soil_router
from api.routers.weather_router import router as weather_router
from api.routers.user_router import router as user_router
from api.routers.limiter import limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from api.config import settings


# Database Configurations
# client = AsyncIOMotorClient(os.getenv('DB_URL'))
uri = os.getenv('DB_URL') 
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)




cred = credentials.Certificate('smart-gardening-system-auth_service_account_keys.json')
'firebase = firebase_admin.initialize_app(cred)'
pb = pyrebase.initialize_app(json.load(open('firebase_config.json')))

app = FastAPI()

app.include_router(plant_router)
app.include_router(soil_router)
app.include_router(weather_router)
app.include_router(user_router)

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


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    async with some_async_resource(): # type: ignore
        print("Run at startup!")
        yield
        print("Run on shutdown!")

@app.get("/")
def read_root():
    return Response("Server is running.")


# signup endpoint
@app.post("/signup", include_in_schema=False)
async def signup(request: Request):
    req = await request.json()
    email = req['email']
    password = req['password']
    if email is None or password is None:
        return HTTPException(detail={'message': 'Error! Missing Email or Password'}, status_code=400)
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return JSONResponse(content={'message': f'Successfully created user {user.uid}'}, status_code=200)    
    except:
        return HTTPException(detail={'message': 'Error Creating User'}, status_code=400)
    
# login endpoint
@app.post("/login", include_in_schema=False)
async def login(request: Request):
    req_json = await request.json()
    email = req_json['email']
    password = req_json['password']
    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user['idToken']
        return JSONResponse(content={'token': jwt}, status_code=200)
    except:
        return HTTPException(detail={'message': 'There was an error logging in'}, status_code=400)
# ping endpoint
# ping endpoint
@app.post("/ping", include_in_schema=False)
async def validate(request: Request):
    headers = request.headers
    jwt = headers.get('authorization')
    print(f"jwt:{jwt}")
    user = auth.verify_id_token(jwt)
    return user["uid"]


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT
    )