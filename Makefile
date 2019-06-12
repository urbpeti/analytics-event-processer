.PHONY: test

build:
	docker-compose build

start:
	docker-compose up

startd:
	docker-compose up -d

down:
	docker-compose down

provision:
	docker-compose run --rm app pipenv run python manage.py provisiondb
	docker-compose run --rm -e APP_SETTINGS="app.config.TestingConfig" app pipenv run python manage.py provisiondb

test:
	docker-compose run --rm -e APP_SETTINGS="app.config.TestingConfig" app pipenv run python -m unittest discover -s ./ -p "*_test.py"

restart:
	make down
	make start