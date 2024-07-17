from typing import List
from fastapi import APIRouter, Request, HTTPException
from ..models import PlantIdentification
from .limiter import limiter
from kindwise import PlantApi, PlantIdentification, UsageInfo
import os
import requests

router = APIRouter(
    prefix="/plants",
)

api = PlantApi(api_key=os.getenv("ADMINKINDWISE_API_KEY"))

# Plant Identification
@router.post("/", response_model = PlantIdentification)
@limiter.limit("1/second")
async def identify_plant_from_image(request: Request, plant: PlantIdentification):
    try:
        plant_dict = api.identify(plant.image_url)
        return plant_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/", response_model = List[PlantIdentification])
@limiter.limit("1/second")
async def get_all_identified_plants(request: Request):
    # This endpoint should return a list of all identified plants, not a single plant.
    # However, the current implementation doesn't provide a way to store or retrieve multiple plants.
    # For now, I'll return an empty list.
    return []

@router.get("/{id}", response_model = PlantIdentification)
@limiter.limit("1/second")
async def get_single_plant_by_id(request: Request, id: str):
    try:
        access_token = 'identification_access_token'
        details = ['common_names', 'taxonomy', 'image']
        language = 'de'
        identification: PlantIdentification = api.get_identification(access_token, id, details=details, language=language)
        return identification
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))