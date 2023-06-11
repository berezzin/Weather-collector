import asyncio

from src.config import CITY_SERVICE_API_KEY
from src.services.cities.service import CityService

city_service = CityService(request_headers={'X-Api-Key': CITY_SERVICE_API_KEY})

if __name__ == '__main__':
    asyncio.run(city_service.execute())
