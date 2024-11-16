from opcua import Server
import random
import time

def generate_sensor_data():

    return {
        "tirePressure": random.uniform(30, 35), 
        "speed": random.uniform(0, 120),
        "fuelLevel": random.uniform(10, 100),  
        "temperature": random.uniform(15, 40)  
    }

def setup_opcua_server():
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4841/smartcar/")
    namespace = server.register_namespace("SmartCarSensorData")
    objects = server.get_objects_node()
    car_sensors = objects.add_object(namespace, "CarSensors")
    tire_pressure_node = car_sensors.add_variable(namespace, "TirePressure", 0.0)
    speed_node = car_sensors.add_variable(namespace, "Speed", 0.0)
    fuel_level_node = car_sensors.add_variable(namespace, "FuelLevel", 0.0)
    temperature_node = car_sensors.add_variable(namespace, "Temperature", 0.0)
    
    tire_pressure_node.set_writable()
    speed_node.set_writable()
    fuel_level_node.set_writable()
    temperature_node.set_writable()

    return server, tire_pressure_node, speed_node, fuel_level_node, temperature_node

def main():
    server, tire_pressure_node, speed_node, fuel_level_node, temperature_node = setup_opcua_server()
    server.start()
    print("OPC UA Server started at opc.tcp://0.0.0.0:4841/smartcar/")
    
    try:
        while True:
            sensor_data = generate_sensor_data()
            print(f"Generated sensor data: {sensor_data}")
            
            tire_pressure_node.set_value(sensor_data["tirePressure"])
            speed_node.set_value(sensor_data["speed"])
            fuel_level_node.set_value(sensor_data["fuelLevel"])
            temperature_node.set_value(sensor_data["temperature"])
            
            time.sleep(5)

    except KeyboardInterrupt:
        print("Server stopped by user.")
    
    finally:
        server.stop()
        print("OPC UA server stopped.")

if __name__ == "__main__":
    main()
