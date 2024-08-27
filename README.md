# Rick and Morty

### Requirements:
1. Endpoint, which return random character from the world of Rick and Morty series.
2. Endpoint get 'search_string' as an argument and return list of all characters, who contains the 'search_string' in the name.
3. On regular basic, app downloads data from external service to inner DB.
4. Requests of implemented API should work with local DB (Take data from DB not from Rick & Morty API).

### Technologies to use:
1. Public API: http://rickanmortyapi.com/documentation.
2. Use celery as task scheduler for data synchronization for Rick & Morty API.
3. Python, Django, ORM, PostgreSQL, Git.
4. All endpoints should be documented via Swagger.

### How to run:
- Create venv: 'python -m venv venv'
- Activate it: 'source venv/bin/activate'
- install requirements: 'pip install -r requirements.txt'
- Create new Postgres DB & User
- Copy .env.sample -> .env and populate with all required data
- Run migrations: 'python manage.py migrate'
- Run Redis Server: 'docker run -d -p 6379:6379 redis'
- Run celery worker for tasks handling: 'celery -A rick_and_morty_api worker -l INFO' (for windows 'celery -A rick_and_morty_api worker -l INFO -P solo')
- Run celery beat for task scheduling: 'celery -A rick_and_morty_api beat-| INFO --scheduler django_celery_beat.scheduler:DatabaseScheduler'
- Create schedule for running sync in DB
- Run app: 'python manage.py runserver'
