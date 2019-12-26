build:

prepare:
	pipenv install


test:
	pipenv run pylint index.py
