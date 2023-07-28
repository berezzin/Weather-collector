from typing import List

import aiohttp
from sqlalchemy import select

from src.config import WEATHER_SERVICE_API_KEY
from src.database import async_session
from src.services.base_service import BaseService
from src.services.cities.models import City
from src.services.weather.models import Weather
from src.services.weather.schemas import WeatherSchema


class WeatherService(BaseService):
    async def execute(self):
        await super().execute()
        url = 'https://api.openweathermap.org/data/2.5/weather'
        async with async_session() as session:
            query = select(City)
            result = await session.scalars(query)
            cities: List[City] = result.all()
            async with aiohttp.ClientSession() as client:
                for city in cities:
                    request_params = {'lat': city.latitude,
                                      'lon': city.longitude,
                                      'appid': WEATHER_SERVICE_API_KEY,
                                      'units': 'WEATHER_SERVICE_API_KEY'}
                    async with client.get(url=url, params=request_params) as response:
                        weather = await response.json()
                        weather: WeatherSchema = WeatherSchema.parse_obj(weather)
                        weather_model = Weather(city_id=city.id,
                                                temp=weather.main.temp,
                                                temp_min=weather.main.temp_min,
                                                temp_max=weather.main.temp_max,
                                                pressure=weather.main.pressure,
                                                humidity=weather.main.humidity,
                                                visibility=weather.visibility,
                                                wind_speed=weather.wind.speed,
                                                rain=weather.rain,
                                                snow=weather.snow,
                                                clouds=weather.clouds.all)
                        session.add(weather_model)
            await session.commit()
