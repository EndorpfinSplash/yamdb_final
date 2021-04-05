# yamdb_final
yamdb_final

# Project Title

Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».

## Getting Started

Данные инструкции позволяют развернуть и выполнить предварительную настройку приложения для запуска в среде Docker.

### Prerequisites

Для установки приложения необходимо наличие установленного Docker и командная оболочка bash и БД PostgreSql.


### Installing

В каталоге приложения создайте файл .env установив необходимые значения для подключения к БД.
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Для запуска приложения необходимо в консоли выполнить следующий скрипт:


```
docker-compose up --build -d --force-recreate && 
docker-compose exec -T web python3 manage.py collectstatic --noinput && 
docker-compose exec -T web python3 manage.py migrate --noinput && 
docker-compose exec -T web python3 manage.py loaddata fixtures.json
docker-compose exec -T web python3 manage.py createsuperuser 
```

после этого можно проверить работу приложения выполнив вход по адресу:
[http://localhost:8000/admin/][link]


## Author

* **Andrew Python** - [my github](https://github.com/EndorpfinSplash)


[link]: http://localhost:8000/admin/

https://github.com/EndorpfinSplash/yamdb_final/actions/workflows/yamdb_workflow.yaml/badge.svg