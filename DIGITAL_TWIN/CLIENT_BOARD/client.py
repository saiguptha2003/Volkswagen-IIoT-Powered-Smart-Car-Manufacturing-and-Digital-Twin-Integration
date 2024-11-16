import random
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def generate_simulated_data():
    return {
        "speed": random.uniform(0, 120),               
        "engine_temperature": random.uniform(70, 110),
        "tire_health": random.uniform(0, 100),         
    }

speed_data, engine_temp_data, tire_health_data = [], [], []
time_data = []

fig, (ax_speed, ax_engine_temp, ax_tire_health) = plt.subplots(3, 1, figsize=(10, 8))
fig.suptitle("Digital Twin Model - Real-Time Monitoring")

ax_speed.set_ylim(0, 150)
ax_speed.set_xlim(0, 50)
line_speed, = ax_speed.plot([], [], color="blue", label="Speed (km/h)")
ax_speed.set_ylabel("Speed (km/h)")
ax_speed.legend(loc="upper right")

ax_engine_temp.set_ylim(60, 120)
ax_engine_temp.set_xlim(0, 50)
line_engine_temp, = ax_engine_temp.plot([], [], color="red", label="Engine Temp (°C)")
ax_engine_temp.set_ylabel("Engine Temperature (°C)")
ax_engine_temp.legend(loc="upper right")

ax_tire_health.set_ylim(0, 100)
ax_tire_health.set_xlim(0, 50)
line_tire_health, = ax_tire_health.plot([], [], color="green", label="Tire Health (%)")
ax_tire_health.set_ylabel("Tire Health (%)")
ax_tire_health.legend(loc="upper right")

def update_plot(frame):
    current_data = generate_simulated_data()
    time_data.append(frame)
    speed_data.append(current_data["speed"])
    engine_temp_data.append(current_data["engine_temperature"])
    tire_health_data.append(current_data["tire_health"])

    ax_speed.set_xlim(max(0, frame - 50), frame)
    ax_engine_temp.set_xlim(max(0, frame - 50), frame)
    ax_tire_health.set_xlim(max(0, frame - 50), frame)

    line_speed.set_data(time_data, speed_data)
    line_engine_temp.set_data(time_data, engine_temp_data)
    line_tire_health.set_data(time_data, tire_health_data)

    return line_speed, line_engine_temp, line_tire_health

ani = FuncAnimation(fig, update_plot, frames=range(200), interval=500, blit=True)

plt.tight_layout()
plt.show()
