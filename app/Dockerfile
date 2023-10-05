# NOTE name need to be Dockerfile
FROM python:3.8

RUN mkdir flask-app
WORKDIR /flask-app
COPY . .
RUN pip install poetry
RUN ls
RUN poetry install -vvv --no-dev
ENTRYPOINT [ "sh", "-c", "sleep 10s && poetry run python3 app.py" ]