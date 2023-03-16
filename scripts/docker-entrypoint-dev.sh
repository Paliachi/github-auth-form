#!/bin/bash


echo "Running makemigrations"
python manage.py makemigrations

echo "Running migrations"
python manage.py migrate

#echo "Running migrations for OAuth2"
#python manage.py migrate oauth2_provider

echo "Running server"
python manage.py runserver 0.0.0.0:8000