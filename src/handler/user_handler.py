from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select

from src.db.database import async_session, City
from src.function.functions import get_city_coordinates, haversine

# The model for requesting the addition of a city
class CityCreate(BaseModel):
    name: str

user_router = APIRouter(prefix="/user")

@user_router.post("/cities/", response_model=CityCreate)
async def add_city(city: Annotated[CityCreate, Depends()]):
    latitude, longitude = await get_city_coordinates(city.name)
    if latitude is None or longitude is None:
        raise HTTPException(status_code=400, detail="Failed to retrieve city coordinates")

    async with async_session() as session:
        new_city = City(name=city.name, latitude=latitude, longitude=longitude)
        session.add(new_city)
        await session.commit()
        await session.refresh(new_city)

    return new_city

# Deleting a city
@user_router.delete("/cities/{city_id}")
async def delete_city(city_id: int):
    async with async_session() as session:
        city = await session.get(City, city_id)
        if city is None:
            raise HTTPException(status_code=404, detail="City not found")

        await session.delete(city)
        await session.commit()

    return {"message": "City deleted successfully"}


# Getting 2 nearest cities
@user_router.get("/nearest_cities/")
async def get_nearest_cities(latitude: float, longitude: float):
    async with async_session() as session:
        cities = await session.scalars(select(City))
        cities_list = cities.all()

    if not cities_list:
        raise HTTPException(status_code=404, detail="No cities found in the database")

    # Calculating distances to a given point
    distances = []
    for city in cities_list:
        distance = haversine(latitude, longitude, city.latitude, city.longitude)
        distances.append((city, distance))

    # Sort by distance and select 2 nearest ones
    nearest_cities = sorted(distances, key=lambda x: x[1])[:2]
    return [{"name": city[0].name, "latitude": city[0].latitude, "longitude": city[0].longitude, "distance": city[1]} for city in nearest_cities]



# Getting information about all cities
@user_router.get("/cities/")
async def get_cities():
    async with async_session() as session:
        cities = await session.scalars(select(City))
        return cities.all()