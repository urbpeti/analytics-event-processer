build:
	docker-compose build

start:
	docker-compose up

startd:
	docker-compose up -d

down:
	docker-compose down

restart:
	make down
	make start