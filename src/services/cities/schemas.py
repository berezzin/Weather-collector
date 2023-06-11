from pydantic import BaseModel, Field


class CitySchema(BaseModel):
    name: str = Field(max_length=20)
    latitude: float
    longitude: float
    country: str = Field(max_length=3)
    population: int
