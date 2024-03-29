# syntax=docker/dockerfile:1
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY ./linebot/ /app/

CMD python manage.py migrate && \
  gunicorn linebot.wsgi --bind 0.0.0.0:$PORT