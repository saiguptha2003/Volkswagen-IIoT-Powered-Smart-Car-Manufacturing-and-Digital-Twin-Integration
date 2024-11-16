import time
import random
import paho.mqtt.client as mqtt

mqttc = mqtt.Client()
mqttc.connect("localhost", 1883)
mqttc.loop_start()

try:
    while True:
        random_number = random.randint(1, 100)
        msg_info = mqttc.publish("paho/test/topic", str(random_number), qos=1)
        print(f"Sent message: {random_number}")
        msg_info.wait_for_publish()
        time.sleep(1)

except KeyboardInterrupt:
    print("Publishing stopped by user.")

finally:
    mqttc.disconnect()
    mqttc.loop_stop()
