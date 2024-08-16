# Testcontainers, Python and PyTest

Test-Driven Development with Python, Testcontainers, and pytest

## Create a virtual environment

```shell
python3 -m venv .venv
```

## Activate the virtual environment

```shell
source .venv/bin/activate
```

## Upgrade pip

```shell
pip install --upgrade pip
```

## Install the required packages

```shell
pip install psycopg
pip install pytest
pip install testcontainers
```

## Freeze the requirements

```shell
pip freeze > requirements.txt
```

## Running Tests

```shell
pytest
```


To set this interpreter as the default for all new projects:
