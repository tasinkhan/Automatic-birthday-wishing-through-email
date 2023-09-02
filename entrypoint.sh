#!/usr/bin/env bash


python manage.py migrate

python manage.py runserver 0.0.0.0:8000

# celery -A automated_birthday_wishing worker -l info

# celery -A automated_birthday_wishing beat -l info

