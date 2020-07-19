FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY . /app

WORKDIR /app/app
USER 1000:1000
EXPOSE 5000/tcp

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
