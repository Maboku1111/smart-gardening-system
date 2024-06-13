# Entry code for the application
from odmantic import ObjectId
import uvicorn
'import firebase_admin'
import pyrebase
import json
from firebase_admin import credentials, auth
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings
import requests
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from typing import Optional
import contextlib
'from starlette.applications import Starlette'
'import setuptools'




'''
router = APIRouter()
app.include_router(router)
'''

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
allow_all = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_all,
    allow_credentials=True,
    allow_methods=allow_all,
    allow_headers=allow_all
)

class CommonSettings(BaseSettings):
    APP_NAME: str = "smart-gardening-system"
    DEBUG_MODE: bool = False

class ServerSettings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8001

class DatabaseSettings(BaseSettings):
    DB_URL: str
    DB_NAME: str

class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    stormglass_api_key: str
    openweathermap_api_key: str
    adminkindwise_api_key: str
    agromonitoring_api_key: str

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
    weather_id: Optional[ObjectId] = Field(alias="_id", default=None)
    temperature: float
    humidity: float
    wind_speed: float
    pressure: float


class User(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    name: str
    email: str
    password: str
    gradening_experience: int
    location: str


@contextlib.asynccontextmanager
async def lifespan(app):
    async with some_async_resource(): # type: ignore
        print("Run at startup!")
        yield
        print("Run on shutdown!")

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

# Soil Moisture Data Collection
@app.post("/soil-moisture", response_model = SoilMoistureData, status_code=status.HTTP_201_CREATED)
async def create_new_reading(soil: SoilMoistureData):
    api_url = f"http://api.agromonitoring.com/agro/1.0/soil polyid=5aaa8052cbbbb5000b73ff66appid=bb0664ed43c153aa072c760594d775a7"  
    soil = requests.get(api_url).json()                           
    with client:
        soil = soil.dict()
        return soil

@app.get("/soil-moisture", response_model = SoilMoistureData)
async def get_all_readings(soil: SoilMoistureData):
    return soil

@app.get("/soil-moisture/{soil_id}", response_model = SoilMoistureData)
async def get_single_reading_by_ID(soil_id: int):
    return soil_id


# Plant Identification
@app.post("/plants", response_model = PlantIdentification)
async def identify_plant_from_image(plant: PlantIdentification):
    plant_dict = plant.dict()
    return plant

@app.get("/plants", response_model = PlantIdentification)
async def get_all_identified_plants(plant: PlantIdentification):
    return plant

@app.get("/plants/{id}", response_model = PlantIdentification)
async def get_single_plant_by_id(plant_id: PlantIdentification):
    return plant_id


# Weather Data Integration
@app.get("/weather/{city}", response_model = WeatherData)  # response_model=WeatherData
async def current_weather(city: str):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('OPENWEATHERMAP_API_KEY')}"
    get_weather = requests.get(api_url).json()
    # WeatherData.weather_id = get_weather["weather"]["id"]
    if "weather" in get_weather and "id" in get_weather["weather"]:
        WeatherData.weather_id = get_weather["weather"]["id"]
        WeatherData.temperature = get_weather["main"]["temp"]
        WeatherData.humidity = get_weather["main"]["humidity"]
        WeatherData.wind_speed = get_weather["wind"]["speed"]
        WeatherData.pressure = get_weather["main"]["pressure"]
        return {"weather_id": WeatherData.weather_id, "temp": WeatherData.temperature, "humidity": WeatherData.humidity, "wind_speed": WeatherData.wind_speed, "pressure": WeatherData.pressure}
    else:
        # Handle the case where the key doesn't exist
        # You can print an error message, set a default value, or take any other appropriate action
        print("The 'weather' key or 'id' key does not exist in the 'get_weather' dictionary.")

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
async def update_user_profile(user_id: int):
    return user_id

@app.delete("/users/{user_id}")
async def delete_item(user_id: int):
    return {f"message": "{user_id} deleted successfully"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        reload=settings.DEBUG_MODE,
        port=settings.PORT
    )