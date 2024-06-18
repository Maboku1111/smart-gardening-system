from pydantic import BaseModel, Field
from odmantic import ObjectId
from typing import Optional


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
    gardening_experience: int
    location: str