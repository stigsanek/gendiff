install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml
