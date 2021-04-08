#!/bin/sh

sleep 10

#DJANGO_SUPERUSER_USERNAME=$(grep DJANGO_SUPERUSER_USERNAME .env | cut -d '=')
#DJANGO_SUPERUSER_EMAIL=$(grep DJANGO_SUPERUSER_EMAIL .env | cut -d '=')
#DJANGO_SUPERUSER_PASSWORD=$(grep DJANGO_SUPERUSER_PASSWORD .env | cut -d '=')

#echo "from django.contrib.auth.models import User; User.objects.create_superuser(${DJANGO_SUPERUSER_USERNAME}, ${DJANGO_SUPERUSER_EMAIL}, ${DJANGO_SUPERUSER_PASSWORD})" | python manage.py shell

python manage.py migrate
python manage.py createcachetable
python manage.py collectstatic  --noinput
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin10', 'nafigatort@yandex.ru', 'secretadmina10')" | python manage.py shell
gunicorn api_yamdb.wsgi:application --bind 0.0.0.0:8000

exec "$@"