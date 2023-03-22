# Сервис для просмотра starred-репозиториев

Сервис для просмотра starred-репозиториев пользователя и issues в каждом с возможностью фильтрации по тегам

Реализован на Django, PostgreSQL, Redis, Docker. Также реализована авторизация через GitHub OAuth.

----

## Настройка проекта
1) Необходимо создать рядом с файлом `settings.py` файл `.env`.
Обязательные поля и пример файла `.env`:
```
SECRET_KEY='some_value'
DEBUG=False
ALLOWED_HOSTS=localhost 127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost http://127.0.0.1
GITHUB_KEY='your_github_key_from_github_oauth_app'
GITHUB_SECRET='your_github_secret_from_github_oauth_app'
CACHE_TTL=60 # Значение времени кеша в секундах
DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=githubstarred-db # название БД
POSTGRES_USER=admin # имя пользователя БД
POSTGRES_PASSWORD=admin # пароль пользователя БД
DB_HOST=postgres
DB_PORT=5432
```

## Запуск проекта
1) Из основной папки проекта запустить команду сборки Docker-compose:
`docker-compose up -d --build`

2) Далее запустить команду применения миграций и сбора статики:

`docker-compose exec backend python manage.py migrate`

`docker-compose exec backend python manage.py collectstatic --no-input`

3) Опционально можно создать superuser'a:

`winpty docker-compose exec backend python manage.py createsuperuser`

Готово! Проект развернут в Docker и готов к работе!

## Фото проекта:
!![image](https://user-images.githubusercontent.com/63292154/226596833-9be2cd85-1c49-46fd-b45e-5d36802b1bbb.png)
![image](https://user-images.githubusercontent.com/63292154/226597042-da1c909a-b877-4f66-8525-367b1c1a61c1.png)
