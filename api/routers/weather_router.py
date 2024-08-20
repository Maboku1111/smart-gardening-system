import requests
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
import logging
import os

logging.basicConfig(level=logging.INFO)

class WeatherData(BaseModel):
    weather_id: int
    temperature: float
    humidity: float
    wind_speed: float
    pressure: float

router = APIRouter(
    prefix="/weather",
)

@router.get("/{city}")
async def current_weather(city: str):
    try:
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('OPENWEATHERMAP_API_KEY')}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        # Validate API response keys
        required_keys = ["weather", "main", "wind"]
        if not all(key in data for key in required_keys):
            raise HTTPException(status_code=404, detail="Weather data not found")
        
        # Extract and convert data
        weather_data = WeatherData(
            weather_id=data["weather"][0]["id"],
            temperature=data["main"]["temp"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            pressure=data["main"]["pressure"]
        )
        return weather_data
    except requests.exceptions.RequestException as e:
        logging.error(f"API request error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    except Exception as e:
        logging.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
