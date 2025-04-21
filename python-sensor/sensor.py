import time
import json
import random
import paho.mqtt.client as mqtt
import socket

MQTT_BROKER = "emqx"
MQTT_PORT = 1883
TOPIC = "sensors/data"

client = mqtt.Client(client_id="python-gateway")

# Reintento simple de conexión al broker
for attempt in range(10):
    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        print("Connected to MQTT Broker")
        break
    except (ConnectionRefusedError, socket.gaierror) as e:
        print(f"Connection failed: {e}. Retrying in 3s...")
        time.sleep(3)
else:
    print("Failed to connect after multiple attempts. Exiting.")
    exit(1)

def simulate_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "timestamp": int(time.time() * 1000)
    }

while True:
    payload = simulate_sensor_data()
    client.publish(TOPIC, json.dumps(payload))
    print(f"Published: {payload}")
    time.sleep(5)