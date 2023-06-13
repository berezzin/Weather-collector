from pydantic import BaseModel


class WeatherSchema(BaseModel):
    temp: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    visibility: int
    wind_speed: float
    rain: dict
    snow: dict
    clouds: int
