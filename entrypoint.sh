#!/bin/sh

sleep 10

echo "from django.contrib.auth.models import User; User.objects.create_superuser($DJANGO_SUPERUSER_USERNAME, $DJANGO_SUPERUSER_EMAIL, $DJANGO_SUPERUSER_PASSWORD)" | python manage.py shell

python manage.py migrate
python manage.py createcachetable
python manage.py collectstatic  --noinput
gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000

exec "$@"