from fastapi import APIRouter, Request
from ..models import PlantIdentification
from .limiter import limiter


router = APIRouter(
    prefix="/plants",
)


# Plant Identification
@router.post("/plants", response_model = PlantIdentification)
@limiter.limit("1/second")
async def identify_plant_from_image(request: Request, plant: PlantIdentification):
    plant_dict = plant.model_dump()
    return plant

@router.get("/plants", response_model = PlantIdentification)
@limiter.limit("1/second")
async def get_all_identified_plants(request: Request, plant: PlantIdentification):
    return plant

@router.get("/plants/{id}", response_model = PlantIdentification)
@limiter.limit("1/second")
async def get_single_plant_by_id(request: Request, plant_id: PlantIdentification):
    return plant_id