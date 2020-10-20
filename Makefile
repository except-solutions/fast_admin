all:
	flake8 --config .setup.cfg
	isort **/*.py
	mypy **/*.py
	pytest tests

lint:
	flake8 --config .setup.cfg

sort:
	isort **/*.py

mypy:
	mypy **/*.py

tests:
	pytest tests
