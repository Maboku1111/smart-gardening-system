# Entry code for the application
from odmantic import ObjectId
import uvicorn
'import firebase_admin'
import pyrebase
import json
from firebase_admin import credentials, auth
from fastapi import FastAPI, Request, APIRouter, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field, ValidationError
from pydantic_settings import BaseSettings
import requests
from motor.motor_asyncio import AsyncIOMotorClient
import os
from typing import Optional
import contextlib
from starlette.applications import Starlette
'import setuptools'


router = APIRouter()
'''
app = FastAPI() 

router = APIRouter()
app.include_router(router)
'''

client = AsyncIOMotorClient(os.getenv('DB_URL'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


cred = credentials.Certificate('smart-gardening-system-auth_service_account_keys.json')
'firebase = firebase_admin.initialize_app(cred)'
pb = pyrebase.initialize_app(json.load(open('firebase_config.json')))
app = FastAPI()
allow_all = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all
)

class CommonSettings(BaseSettings):
    APP_NAME: str = "FARM Starter"
    DEBUG_MODE: bool = False

class ServerSettimgs(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 0000

class DatabaseSettings(BaseSettings):
    DB_URL: str
    DB_NAME: str

class Settings(CommonSettings, ServerSettimgs, DatabaseSettings):
    pass

    class Config:
        env_file = ".env"


settings = Settings()

# Data models for MongoDB
class SoilMoistureData(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    device_id: str
    soil_moisture_level: float
    temperatue: float
    humidity: float
    timestamp: str


class PlantIdentification(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    image_url: str
    plant_name: str
    plant_species: str
    confidence_level: str


class WeatherData(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    location: str
    temperature: float
    humidity: float
    wind_speed: float
    precipitation: float
    timpestamp: str

'''
class User(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    name: str
    email: str
    password: str
    gradening_experience: int
    location: str
'''

@contextlib.asynccontextmanager
async def lifespan(app):
    async with some_async_resource(): # type: ignore
        print("Run at startup!")
        yield
        print("Run on shutdown!")

# Database connections
'''
@router.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
    app.mongodb = app.mongodb_client(settings.DB_NAME)

@router.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()
'''

# signup endpoint
@router.post("/signup", include_in_schema=False)
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
@router.post("/login", include_in_schema=False)
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
@router.post("/ping", include_in_schema=False)
async def validate(request: Request):
    headers = request.headers
    jwt = headers.get('authorization')
    print(f"jwt:{jwt}")
    user = auth.verify_id_token(jwt)
    return user["uid"]

# Soil Moisture Data Collection
@router.post("/soil-moisture", response_model = SoilMoistureData, status_code=status.HTTP_201_CREATED)
async def create_new_reading(soil: SoilMoistureData):
    with client:
        soil_dict = soil.dict()
        return soil

@router.get("/soil-moisture", response_model = SoilMoistureData)
async def get_all_readings(soil: SoilMoistureData):
    return soil

@router.get("/soil-moisture/{soil_id}", response_model = SoilMoistureData)
async def get_single_reading_by_ID(soil_id: int):
    return soil_id


# Plant Identification
@router.post("/plants", response_model = PlantIdentification)
async def identify_plant_from_image(plant: PlantIdentification):
    plant_dict = plant.dict()
    return plant

@router.get("/plants", response_model = PlantIdentification)
async def get_all_identified_plants(plant: PlantIdentification):
    return plant

@router.get("/plants/{id}", response_model = PlantIdentification)
async def get_single_plant_by_id(plant_id: PlantIdentification):
    return plant_id


# Weather Data Integration
@router.get("/weather", response_model=WeatherData)
async def current_weather(city: str):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=53de5266d72d0559770b07222286e1af"
    get_weather = requests.get(api_url).json()
    lat = get_weather["coord"]["lat"]
    lon = get_weather["coord"]["lon"]
    return {"latitude": lat, "longitude": lon}



'''
# User Management
@app.post("/users", response_model = User)
async def create_new_user(user: User):
    return user

@app.get("/users", response_model = User)
async def get_all_users(user: User):
    return user

@app.get("/users/{user_id}", response_model = User)
async def get_single_user_by_id(user_id: int):
    return user_id

@app.patch("/users/{user_id}", response_model = User)
async def update_user_profile(user_id: int, user: User):
    return user

@app.delete("/users/{user_id}")
async def delete_item(user_id: int):
    return {"message": "Item deleted successfully"}
'''

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT
    )