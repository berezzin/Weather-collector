FROM python:3.11

RUN mkdir 'app'

WORKDIR /app

RUN pip install poetry

COPY poetry.lock pyproject.toml ./

RUN poetry install --no-root

COPY . .
