import asyncio
import logging

from src.config import CITY_SERVICE_API_KEY
from src.services.cities.service import CityService

logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)

city_service = CityService(request_headers={'X-Api-Key': CITY_SERVICE_API_KEY})

if __name__ == '__main__':
    logging.info('Loading city data...')
    asyncio.run(city_service.execute())
    logging.info('Cities have been loaded')
