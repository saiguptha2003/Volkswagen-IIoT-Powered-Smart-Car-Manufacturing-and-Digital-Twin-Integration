import time
from opcua import Client as OPCUAClient
import paho.mqtt.client as mqtt
import json

opc_client = OPCUAClient("opc.tcp://10.1.14.11:4841/")
opc_client.connect()
print("Connected to OPC UA Server")

mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883)
mqtt_client.loop_start()
print("Connected to MQTT Broker")

try:
    uri = "http://examples.opcua/python-opcua"
    idx = opc_client.get_namespace_index(uri)

    temperature_node = opc_client.get_node("ns=2;i=2")

    while True:
        temp_value = temperature_node.get_value()
        timestamp = time.time()
        payload = {
            "timestamp": timestamp,
            "temperature": temp_value
        }
        payload_json = json.dumps(payload)
        msg_info = mqtt_client.publish("paho/test/topic", payload_json, qos=1)
        msg_info.wait_for_publish()
        print(f"Published to MQTT: {payload_json}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Middleware stopped by user.")

finally:
    opc_client.disconnect()
    print("Disconnected from OPC UA Server.")
    mqtt_client.disconnect()
    mqtt_client.loop_stop()
    print("Disconnected from MQTT Broker.")
