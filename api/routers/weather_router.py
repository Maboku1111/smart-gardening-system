from fastapi import APIRouter, Request
from ..models import WeatherData
from .limiter import limiter
import requests
import os

router = APIRouter(
    prefix="/weather",
)

# Weather Data Integration
@router.get("/weather/{city}", response_model = WeatherData)
@limiter.limit("1/second")
async def current_weather(request: Request, city: str):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('OPENWEATHERMAP_API_KEY')}"
    get_weather = requests.get(api_url).json()
    if "weather" in get_weather and "id" in get_weather["weather"]:
        weather_data = WeatherData(
            weather_id = get_weather["weather"]["id"],
            temperature = get_weather["main"]["temp"],
            humidity = get_weather["main"]["humidity"],
            wind_speed = get_weather["wind"]["speed"],
            pressure = get_weather["main"]["pressure"]
        )
        return weather_data
    else:
        print("The 'weather' key or 'id' key does not exist in the 'get_weather' dictionary.")
        return None