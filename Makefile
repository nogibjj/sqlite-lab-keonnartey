install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	#disable comment to test speed
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	#ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

run:
	python main.py

extract:
	python main.py --extract

transform_load:
		python main.py --load

query:
	python main.py --query

generate_and_push:
			python main.py --generate_and_push

deploy:
	#extract, transform, load, query
	python -m main --extract --load --query
		
all: install lint test format
