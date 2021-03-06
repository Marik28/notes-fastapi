install:
	pip install -r requirements.txt

run-dev:
	cd src; python -m notes_api

drop-test-db:
	dropdb test_db --if-exists

create-test-db:
	export POSTGRES_DB_NAME='test_db'; createdb test_db; cd src; python scripts.py create-tables

# todo придумать нормальные зависимости
test: drop-test-db create-test-db
	export PYTHONPATH=$$(pwd)/src; export POSTGRES_DB_NAME='test_db'; pytest -s

create-jwt-secret:
	cd src; python scripts.py create-jwt-secret