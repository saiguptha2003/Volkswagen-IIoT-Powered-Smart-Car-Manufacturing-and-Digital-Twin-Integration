from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

@app.route('/data')
def get_data():
    data = []
    for i in range(100):
        data.append({
            "timestamp": (datetime.now() - timedelta(minutes=i)).strftime('%Y-%m-%d %H:%M:%S'),
            "tirePressure": random.uniform(30, 35),
            "speed": random.uniform(0, 120),
            "fuelLevel": random.uniform(10, 100),
            "temperature": random.uniform(15, 40)
        })

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
