build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f todo

migrate:
	docker-compose run --rm todo python manage.py migrate

makemigrations:
	docker-compose run --rm todo python manage.py makemigrations

clean:
	docker-compose down -v --rmi local --remove-orphans