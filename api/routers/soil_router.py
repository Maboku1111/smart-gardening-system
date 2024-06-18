from fastapi import APIRouter, status, Request
from ..models import SoilMoistureData
from .limiter import limiter
import requests


router = APIRouter(
    prefix="/soil",
)


# Soil Moisture Data Collection
@router.post("/soil-moisture", response_model = SoilMoistureData, status_code=status.HTTP_201_CREATED)
@limiter.limit("1/second")
async def create_new_reading(request: Request, soil: SoilMoistureData):
    api_url = f"http://api.agromonitoring.com/agro/1.0/soil polyid=5aaa8052cbbbb5000b73ff66appid=bb0664ed43c153aa072c760594d775a7"  
    soil = requests.get(api_url).json()                           
    with client:
        soil = soil.dict()
        return soil

@router.get("/soil-moisture", response_model = SoilMoistureData)
@limiter.limit("1/second")
async def get_all_readings(request: Request, soil: SoilMoistureData):
    return soil

@router.get("/soil-moisture/{soil_id}", response_model = SoilMoistureData)
@limiter.limit("1/second")
async def get_single_reading_by_ID(request: Request, soil_id: int):
    return soil_id