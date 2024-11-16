# IloT-Powered Smart Car Manufacturing and Digital Twin Integration

This project explores the integration of Industrial Internet of Things (IIoT) and Digital Twin technology to revolutionize the car manufacturing process and smart car. The goal is to enhance production efficiency, real-time performance monitoring, and data-driven decision-making by leveraging connected devices and virtual models.
 
## Project Overview
- **IloT in Manufacturing**: Enhancing efficiency through connected devices.
- **Digital Twin**: Creating a virtual model of a physical car for real-time simulation.
- **Machine Learning & Predictive Modeling**: Predicting maintenance needs and optimizing production processes.
- **Technologies Used**: FastAPI, Flask, React, Figma, MQTT, OPC UA, Python.

## Agenda
1. Introduction to IIoT in Manufacturing
2. Project Objectives
3. Role of OPC Server in Data Publishing
4. Overview of Digital Twin Technology
5. System Architecture


## System Architecture

### IloT-Powered Smart Car Manufacturing
1. **Sensors**: Sensors collect data on machine performance, production efficiency, and environmental conditions.
2. **OPC Server**: Aggregates and publishes data from sensors.
3. **Cloud Integration**: Data is sent to the cloud for storage and analysis.
4. **Actuator Control**: Commands sent to the production process based on insights.
5. **SCADA**: Centralized control and visualization of production processes.

### Digital Twin Integration for Cars
1. **Sensor Installation**: Sensors on the car collect real-time data on engine, tire, and environmental conditions.
2. **OPC Server**: Standardizes communication between sensor devices.
3. **Digital Twin Model**: Virtual representation of the car reflecting real-time data.
4. **Continuous Monitoring**: Continuous updates of the digital twin model.
5. **Feedback Loop**: Use insights from the digital twin for real-time adjustments.

## Technologies Used
- **Backend**:
  - FastAPI: Lightweight Python framework for fast development.
  - Flask: Python framework for creating the web API.
  - OPC UA, MQTT: Communication protocols for sensor data exchange.
- **Frontend**:
  - React: For developing the user interface.
  - Figma: For designing the digital twin model.

## Machine Learning & Predictive Modeling (Not Implemented yet due to Insufficient Resources)

1. **Data Collection and Preparation**:
   - Collect real-time data from car sensors (engine performance, tire health, etc.).
   
2. **Model Training**:
   - Train ML algorithms on historical data (e.g., using `scikit-learn`).
   - Use regression models or time-series forecasting to predict future behaviors like maintenance needs.

3. **Predictive Analytics**:
   - Apply trained models to real-time data from the car to predict possible failures (e.g., engine overheating, tire wear).
   - Use time-series models or classification algorithms for predicting maintenance.

4. **Actionable Insights**:
   - Real-time alerts and recommendations for predictive maintenance.
   - Use a dashboard for visualizing vehicle performance and system health.

## Cloud Integration
- The system sends data to a cloud platform (AWS, Azure, etc.) for:
  - Data storage
  - Advanced processing and analytics
  - Real-time monitoring

## Quick Setup

### Prerequisites
- Python 3.7 or later
- Node.js and npm (for React)
- Docker (for cloud integration)

### Backend (FastAPI + Flask)
1. Clone the repository Backend:
    ```bash
    git clone https://github.com/saiguptha2003/Volkswagen-IIoT-Powered-Smart-Car-Manufacturing-and-Digital-Twin-Integration.git
    cd Volkswagen-IIoT-Powered-Smart-Car-Manufacturing-and-Digital-Twin-Integration
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI app:
    ```bash
    uvicorn fastapi_app:app --reload
    ```

4. Run the Flask app:
    ```bash
    python server.py
    ```

### Frontend (React)
1. Install frontend dependencies:
    ```bash
    git clone https://github.com/saiguptha2003/Volkswagen-SCADA-Tool-Frontend.git
    cd Volkswagen-SCADA-Tool-Frontend
    npm install
    ```

2. Start the React app:
    ```bash
    npm start
    ```

### Machine Learning (Python) (Not implemented yet due to insufficient resources)
1. Install ML dependencies:
    ```bash
    pip install scikit-learn pandas numpy
    ```

2. Train the model using sample data and save it to a file:
    ```python
    from sklearn.linear_model import LinearRegression
    import pandas as pd

    data = pd.read_csv("sensor_data.csv")
    model = LinearRegression()
    model.fit(data[['sensor1', 'sensor2']], data['output'])
    ```

3. Use the trained model for predictions:
    ```python
    prediction = model.predict(new_sensor_data)
    ```
## Outputs
![Alt text](https://github.com/saiguptha2003/Volkswagen-IIoT-Powered-Smart-Car-Manufacturing-and-Digital-Twin-Integration/blob/main/outputs/digitaltwin.png)
![Alt text](https://github.com/saiguptha2003/Volkswagen-IIoT-Powered-Smart-Car-Manufacturing-and-Digital-Twin-Integration/blob/main/outputs/scadatool.png)
## Future Enhancements
- Expand the machine learning models for more accurate predictive maintenance.
- Integrate more sensors for detailed data collection.
- Enhance the Digital Twin model to simulate vehicle behavior in more complex scenarios.

## Contributing
Feel free to fork this project, submit issues, and contribute enhancements.

## License
MIT License
