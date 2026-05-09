--Codigo base proyecto
CREATE TABLE IF NOT EXISTS readings (
    id SERIAL PRIMARY KEY,
    temperature FLOAT,
    humidity FLOAT,
    pm25 FLOAT,
    pm10 FLOAT,
    co FLOAT,
    o3 FLOAT,
    aqi_status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO readings (temperature, humidity, pm25, pm10, co, o3, aqi_status)
VALUES
(25.3, 48, 28, 35, 210, 31, 'Moderate'),
(24.9, 50, 18, 24, 180, 27, 'Good'),
(26.1, 46, 42, 55, 240, 38, 'Moderate');
