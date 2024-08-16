# testcontainer-python-demo

An example Python Testcontainers project


## Setup

Create a virtual environment

```shell
python3 -m venv .venv
```

Activate the virtual environment

```shell
source .venv/bin/activate
```

Upgrade pip

```shell
pip install --upgrade pip
```

Install the required packages

```shell
pip install psycopg
pip install pytest
pip install testcontainers
```

Freeze the requirements

```shell
pip freeze > requirements.txt
```

## Running Tests

```shell
pytest
```

## Issues


### Handling the postgres error that keeps coming up on systems without Postgres installed

I kept getting an error when trying to run the tests:

```text
E   ImportError: no pq wrapper available.
E   Attempts made:
E   - couldn't import psycopg 'c' implementation: No module named 'psycopg_c'
E   - couldn't import psycopg 'binary' implementation: No module named 'psycopg_binary'
E   - couldn't import psycopg 'python' implementation: libpq library not found
```

To resolve it I tried this.

```shell
brew install postgresql
```

That seemed to work.

### Handling the urllib3 issue on MacOS with Python 3.9


Because of issues with requests and urllib3, I am trying to install
Python 3.12 from homebrew as follows:

```bash
brew install python@3.12
```

To ensure you are using the proper version of Python, edit your ~/.zshrc file
to include the following:

```bash
export PATH="/usr/local/opt/python@3.12/bin:$PATH"
```

Then make sure to reload your shell configuration

```bash
source ~/.zshrc
```

Verify the version of Python you are using

```bash
python3 --version
```

Also in PyCharm I had to create a new local interpreter and point it to

```/opt/homebrew/Cellar/python@3.12/3.12.4/bin/python3.12```

To set the default Python interpreter in PyCharm to the one located at /opt/homebrew/Cellar/python@3.12/3.12.4/bin/python3.12, follow these steps:  

1. Open PyCharm. 
2. Go to PyCharm > Preferences (or File > Settings on Windows/Linux). 
3. Navigate to Project: <Your Project Name> > Python Interpreter. 
4. Click on the gear icon next to the current interpreter and select Add.... 
5. Choose System Interpreter. 
6. Browse to /opt/homebrew/Cellar/python@3.12/3.12.4/bin/python3.12 and select it. 
7. Click OK to apply the changes.

To set this interpreter as the default for all new projects: