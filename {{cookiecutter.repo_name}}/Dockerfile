FROM python:{{cookiecutter.python_version}}-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt  --no-cache-dir

RUN python setup.py install