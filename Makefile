dev:
	uvicorn src.main:app --reload --port 8000 --host 127.0.0.1

prod:
	uvicorn src.main:app --port 8000 --host 0.0.0.0

format:
	ruff check .
	ruff fix .

compose:
	docker-compose build
	docker-compose up

migrate:
	alembic upgrade head

create-migration:
	alembic revision --autogenerate -m '${msg}'