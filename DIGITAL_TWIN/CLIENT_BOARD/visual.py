import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.colors import rgb_to_hsv, hsv_to_rgb
from matplotlib.animation import FuncAnimation

engine_img = mpimg.imread('engine.jpg')
tire_img = mpimg.imread('tire.jpg')

def simulate_data():
    return {
        "speed": random.uniform(0, 120),
        "engine_temperature": random.uniform(70, 110),
        "tire_health": random.uniform(0, 100),
    }

def color_tint(image, tint_factor):
    tinted_image = image.copy()
    for i in range(tinted_image.shape[0]):
        for j in range(tinted_image.shape[1]):
            pixel = tinted_image[i, j, :3]
            hsv_pixel = rgb_to_hsv(pixel / 255.0) 
            hsv_pixel[0] = tint_factor
            tinted_image[i, j, :3] = hsv_to_rgb(hsv_pixel) * 255.0 
    return tinted_image

fig, ax = plt.subplots(figsize=(8, 6))
ax.axis("off")
engine_display = ax.imshow(engine_img, extent=[-2, -1, -1, 1])
tire_display = ax.imshow(tire_img, extent=[1, 2, -1, 1])

def update(frame):
    data = simulate_data()
    engine_temp = data["engine_temperature"]
    tire_health = data["tire_health"]

    if engine_temp < 80:
        engine_display.set_data(color_tint(engine_img, 0.5))
    elif 80 <= engine_temp <= 100:
        engine_display.set_data(color_tint(engine_img, 0.3))
    else:
        engine_display.set_data(color_tint(engine_img, 0.1))

    if tire_health > 70:
        tire_display.set_data(color_tint(tire_img, 0.3))
    elif 40 <= tire_health <= 70:
        tire_display.set_data(color_tint(tire_img, 0.15))
    else:
        tire_display.set_data(color_tint(tire_img, 0.05))

    ax.set_title(f"Speed: {data['speed']:.1f} km/h | Engine Temp: {engine_temp:.1f}°C | Tire Health: {tire_health:.1f}%")

ani = FuncAnimation(fig, update, frames=range(100), interval=1000)
plt.show()
