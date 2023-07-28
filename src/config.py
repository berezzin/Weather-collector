from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

CITY_SERVICE_API_KEY = os.getenv('CITY_SERVICE_API_KEY')
WEATHER_SERVICE_API_KEY = os.getenv('WEATHER_SERVICE_API_KEY')
