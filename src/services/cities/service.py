from typing import List

import aiohttp
from pydantic import parse_obj_as
from sqlalchemy import select, func

from src.database import async_session
from src.services.base_service import BaseService
from src.services.cities.models import City
from src.services.cities.schemas import CitySchema


class CityService(BaseService):
    def __init__(self, request_headers: dict):
        self.request_headers: dict = request_headers

    async def execute(self, params=None):
        if params is None:
            params = {'min_population': 1, 'limit': 30}
        await super().execute()
        async with async_session() as session:
            query = select(func.count()).select_from(City)
            result = await session.scalars(query)
            city_count = result.all()[0]
            if city_count == 0:  # Execute if city table is empty
                async with aiohttp.ClientSession(headers=self.request_headers) as client:
                    url = f'https://api.api-ninjas.com/v1/city'
                    async with client.get(url=url, params=params) as response:
                        cities: list = await response.json()
                        cities: list[CitySchema] = parse_obj_as(List[CitySchema], cities)
                        for city in cities:
                            new_city = City(name=city.name,
                                            latitude=city.latitude,
                                            longitude=city.longitude,
                                            country=city.country,
                                            population=city.population)
                            session.add(new_city)
                await session.commit()
            elif city_count < 50:  # Execute if city table less, than 50 required results
                pass
