Weather Collector is a service that collects all weather data every hour from the 50 largest cities in the world. Based on this data, the power of data centers will be managed in terms of cooling and load.

This service is provided using the following technology stack:
* Celery
* Postres
* Redis
* SQLAlchemy
* Alembic
* Pydantic

If you are impressed and want to deploy this wonderfull service on your server you just need 3 steps:

1. Clone this repo
2. Get and activate [CITY_SERVICE_API_KEY](https://api-ninjas.com/), [WEATHER_SERVICE_API_KEY](https://openweathermap.org/guide)
3. Create in the root folder of project `.env-non-dev` file with required environment variables as in example bellow
![image](https://github.com/berezzin/Weather-collector/assets/101830798/e28f135b-6fb9-46f8-9312-532db19ccc09)
4. Run `docker-compose -f docker-compose-prod.yaml up` command inside the root folder of repository and enjoy the service.
