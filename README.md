# Django + Docker quickstart
Easy setup for development or production environment

### This initiative is a union of two other projects:
- [Django Quickstart](https://github.com/henriquebastos/django-quickstart/)
- [Django on Docker](https://github.com/testdrivenio/django-on-docker)

### This project contains
- Python 3.11 (Dockerfile.dev / Dockerfile.prod)
- [Python Decouple](https://pypi.org/project/python-decouple/)
- [Dj Database URL](https://pypi.org/project/dj-database-url/)
- [Gunicorn](https://pypi.org/project/gunicorn/)
- Support to PostgreSQL with [psycopg-binary](https://pypi.org/project/psycopg-binary/)
- Support to pytest and pytest-django

## One command
```bash
PROJECT_NAME=myProject && \
python -m venv .venv && \
source .venv/bin/activate && \
python -m pip install --upgrade pip && \
python -m pip install django
django-admin startproject --template https://github.com/allansbo/django-docker-quickstart/archive/master.zip --name=.env.dev,.env.prod,pytest.ini,docker-compose.prod.yml $PROJECT_NAME . && \
pip install --prefer-binary -r app/requirements-dev.txt && \
git init && \
git add . && \
git commit -m 'Initial import'
```

**Important!** Update the .env files with your settings

## Development
Uses the default Django development server.
```docker-compose
docker-compose -f docker-compose.dev.yml up -d --build
```
- Run at http://localhost:8000/

## Production
Uses gunicorn + nginx.
```docker-compose
docker-compose -f docker-compose.prod.yml up -d --build
```
- Run at http://localhost:80