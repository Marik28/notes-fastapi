install:
	pip install -r requirements.txt

run-dev:
	cd src; python -m notes_api

test:
	export PYTHONPATH=$$(pwd)/src; export POSTGRES_DB_NAME='test_db'; pytest
