FROM python:3.11

RUN mkdir 'app'

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . .

CMD poetry run alembic upgrade head && poetry run celery -A main worker -B -l INFO