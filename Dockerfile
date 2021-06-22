# syntax=docker/dockerfile:1

FROM python:3.9.5-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY app.py .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
