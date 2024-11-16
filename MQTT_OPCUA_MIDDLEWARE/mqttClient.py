import json
import time
import pandas as pd
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "paho/test/topic"

data_list = []

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe(MQTT_TOPIC)
        print(f"Subscribed to topic: {MQTT_TOPIC}")
    else:
        print(f"Failed to connect with result code {rc}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        print(f"Received message: {payload}")
        record = {
            "value": payload.get("temperature"),
            "opcua_timestamp": payload.get("timestamp"),
            "received_timestamp": time.time()
        }
        data_list.append(record)
    except Exception as e:
        print(f"Error processing message: {e}")

def save_to_csv():
    if data_list:
        df = pd.DataFrame(data_list)
        df.to_csv("mqtt_data.csv", mode="a", header=not pd.io.common.file_exists("mqtt_data.csv"), index=False)
        data_list.clear()
        print("Data saved to mqtt_data.csv")

mqtt_client = mqtt.Client()

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

try:
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
    mqtt_client.loop_start()

    print("Waiting for data...")

    # Allow time for the client to connect and subscribe to the topic
    time.sleep(2)

    while True:
        time.sleep(5)  # Saving data to CSV periodically
        save_to_csv()  # Save any collected data to the CSV file

except KeyboardInterrupt:
    print("Program interrupted. Saving remaining data...")
finally:
    mqtt_client.loop_stop()
    save_to_csv()
    mqtt_client.disconnect()
    print("Disconnected from MQTT broker and data saved.")
