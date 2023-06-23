FROM python:3.9.17-alpine3.18

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY app /code/app/
COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry install
