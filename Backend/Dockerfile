FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn --bind 0.0.0.0:$PORT main:app  # Assuming your app instance is named "app" in main.py
