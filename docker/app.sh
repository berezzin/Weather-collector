#!/bin/bash

alembic upgrade head

celery -A main worker -B -l INFO