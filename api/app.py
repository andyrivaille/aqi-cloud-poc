from flask import Flask, jsonify

app = Flask(__name__)

# Datos simulados AQI
latest_reading = {
    "temperature": 25.3,
    "humidity": 48,
    "pm25": 28,
    "pm10": 35,
    "co": 210,
    "o3": 31,
    "aqi_status": "Moderate"
}

@app.route("/")
def home():
    return jsonify({
        "project": "AQI Monitoreo PoC",
        "status": "running",
        "message": "Middleware API funcionando correctamente"
    })

@app.route("/api/latest")
def latest():
    return jsonify(latest_reading)

@app.route("/api/summary")
def summary():
    return jsonify({
        "location": "DCEyC",
        "devices": 1,
        "active_sensors": [
            "PM2.5",
            "PM10",
            "CO",
            "O3",
            "Temperature",
            "Humidity"
        ],
        "aqi_status": latest_reading["aqi_status"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
