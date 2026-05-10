from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.route("/")
def home():
    return jsonify({
        "project": "AQI Cloud Monitoring PoC",
        "status": "running",
        "database": "connected"
    })

@app.route("/api/latest")
def latest():

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT temperature, humidity, pm25, pm10, co, o3, aqi_status
            FROM readings
            ORDER BY id DESC
            LIMIT 1;
        """)

        row = cur.fetchone()

        cur.close()
        conn.close()

        if row:
            return jsonify({
                "temperature": row[0],
                "humidity": row[1],
                "pm25": row[2],
                "pm10": row[3],
                "co": row[4],
                "o3": row[5],
                "aqi_status": row[6]
            })

        return jsonify({"message": "No data found"})

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api/summary")
def summary():

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT COUNT(*) FROM readings;")
        total = cur.fetchone()[0]

        cur.close()
        conn.close()

        return jsonify({
            "project": "AQI Cloud Monitoring PoC",
            "records": total,
            "database": "PostgreSQL Cloud"
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

