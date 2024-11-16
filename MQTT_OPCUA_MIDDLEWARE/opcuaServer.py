import time
from opcua import Server
import paho.mqtt.client as mqtt
from w1thermsensor import W1ThermSensor

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:4841/freeopcua/server/")

uri = "http://examples.opcua/python-opcua"
idx = server.register_namespace(uri)

objects = server.get_objects_node()
myobj = objects.add_object(idx, "MyObject")

temperature = myobj.add_variable(idx, "Temperature", 0)
temperature.set_writable()

sensor = W1ThermSensor()

mqtt_broker = "mqtt.eclipse.org"
mqtt_port = 1883
mqtt_topic = "home/sensor/temperature"

client = mqtt.Client()
client.connect(mqtt_broker, mqtt_port, 60)

server.start()
print("OPC UA Server started at {}".format(server.endpoint))

try:
    while True:
        temperature_in_celsius = sensor.get_temperature()
        print(f"New temperature value: {temperature_in_celsius}°C")
        
        temperature.set_value(temperature_in_celsius)
        
        client.publish(mqtt_topic, temperature_in_celsius)
        
        time.sleep(1)

except KeyboardInterrupt:
    print("Server stopped.")
finally:
    server.stop()
    print("OPC UA Server stopped.")
