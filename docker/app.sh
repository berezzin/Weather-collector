#!/bin/bash

poetry run alembic upgrade head

poetry run celery -A main worker -B -l INFO