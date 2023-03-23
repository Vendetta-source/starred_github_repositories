# Сервис для просмотра starred-репозиториев

Сервис для просмотра starred-репозиториев пользователя и issues в каждом с возможностью фильтрации по тегам

Реализован на Django, PostgreSQL, Redis, Docker. Также реализована авторизация через GitHub OAuth.

----

## Настройка проекта
1) Создать GitHub OAuth App.

В поле Homepage URL указать: `http://127.0.0.1:8000/`

В поле Authorization callback URL указать: `http://127.0.0.1:8000/social/complete/github/`

2) Необходимо создать рядом с файлом `settings.py` файл `.env`.
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

`docker-compose exec backend python manage.py createsuperuser`

Готово! Проект развернут в Docker и готов к работе!

## Фото проекта:

![image](https://user-images.githubusercontent.com/63292154/226618974-a122fe66-e5f4-4de2-a830-dae504e017c9.png)
![image](https://user-images.githubusercontent.com/63292154/226619224-4847d8b4-d0f7-4815-ac6c-53c4482699a2.png)
![image](https://user-images.githubusercontent.com/63292154/226619825-949adc4a-d531-4b3f-a4c7-91b53786c81c.png)

