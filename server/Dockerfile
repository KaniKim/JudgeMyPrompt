FROM python:3.12-slim

ENV TZ Asia/Seoul
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV POETRY_VERSION=1.8.3

RUN pip install -U pip setuptools && pip install poetry==${POETRY_VERSION}



COPY ./poetry.lock ./poetry.lock
COPY ./pyproject.toml ./pyproject.toml

RUN poetry install

COPY ./pyproject.toml ./poetry.lock ./alembic.ini /app/
ENV PYTHONPATH=/usr/local/bin/python3.12
RUN chmod +x /usr/local/bin/poetry
RUN sed -i '1s|^.*$|#!/usr/local/bin/python3.12|' /usr/local/bin/poetry
RUN ls -l /usr/local/bin/poetry

WORKDIR /app

EXPOSE 8000