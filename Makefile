install:
	pip install --upgrade pip
	pip install -r requirements.txt


freeze:
	pip freeze > requirements.txt

test:
	pytest -v
