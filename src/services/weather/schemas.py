from pydantic import BaseModel


class WeatherMain(BaseModel):
    temp: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


class WeatherWind(BaseModel):
    speed: float


class WeatherClouds(BaseModel):
    all: int


class WeatherSchema(BaseModel):
    main: WeatherMain
    visibility: int
    wind: WeatherWind
    rain: dict | None
    snow: dict | None
    clouds: WeatherClouds
