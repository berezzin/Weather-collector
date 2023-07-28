import asyncio
import logging

from src.config import CITY_SERVICE_API_KEY
from src.services.cities.service import CityService
from src.services.weather.service import WeatherService

logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)

city_service = CityService(request_headers={'X-Api-Key': CITY_SERVICE_API_KEY})
weather_service = WeatherService()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    logging.info('Loading city data...')
    loop.run_until_complete(city_service.execute())
    logging.info('Cities have been loaded')
    logging.info('Loading weather by each city...')
    loop.run_until_complete(weather_service.execute())
    logging.info('Weather has been successfully loaded')
