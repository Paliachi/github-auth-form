SHELL := /bin/bash

help:
    @$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

migration:
    python manage.py makemigrations

migrate:
    python manage.py migrate

superuser:
    python manage.py createsuperuser

deploy:
    docker-compose build
    docker-compose up -d

down:
    docker-compose down

up:
    docker-compose up
