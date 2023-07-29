import asyncio
import logging
from datetime import timedelta

from celery import Celery
from celery.signals import worker_ready

from src.config import REDIS_HOST, REDIS_PORT, CITY_SERVICE_API_KEY
from src.services.cities.service import CityService
from src.services.weather.service import WeatherService

logging.basicConfig(format='[%(asctime)s] %(message)s', datefmt='%d.%m.%Y %H:%M:%S', level=logging.INFO)

app = Celery(broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')
app.conf.beat_schedule = {'run-every-hour':
                              {'task': 'main_task',
                               'schedule': timedelta(hours=1)}}


@worker_ready.connect
def at_start(sender, **kwargs):
    """Run tasks at startup"""
    with sender.app.connection() as conn:
        sender.app.send_task("main_task", connection=conn)


city_service = CityService(request_headers={'X-Api-Key': CITY_SERVICE_API_KEY})
weather_service = WeatherService()


@app.task(name='main_task')
def main():
    loop = asyncio.get_event_loop()
    logging.info('Loading city data...')
    loop.run_until_complete(city_service.execute())
    logging.info('Cities have been loaded')
    logging.info('Loading weather by each city...')
    loop.run_until_complete(weather_service.execute())
    logging.info('Weather has been successfully loaded')


if __name__ == '__main__':
    main()
