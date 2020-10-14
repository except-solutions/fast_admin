all:
	flake8 --config .setup.cfg
	isort **/*.py

lint:
	flake8 --config .setup.cfg

sort:
	isort **/*.py

mypy:
	mypy **/*.py
