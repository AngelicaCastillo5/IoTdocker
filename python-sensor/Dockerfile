FROM python:3.11-slim

WORKDIR /app

COPY sensor.py .

RUN pip install paho-mqtt

CMD ["python", "sensor.py"]
