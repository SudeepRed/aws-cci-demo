# NOTE name need to be Dockerfile
FROM python:3.8

RUN mkdir flask-app
WORKDIR /flask-app
COPY . .
RUN pip install poetry
RUN poetry install -vvv --no-dev