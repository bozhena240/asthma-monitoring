import csv
import random
from datetime import datetime, timedelta


def calculate_risk(data):
    if data["spo2"] < 94 and data["air_quality_raw"] > 700:
        return "HIGH", "Low SpO2 combined with poor air quality"

    if data["spo2"] < 94:
        return "HIGH", "SpO2 is below the safety threshold"

    if data["air_quality_raw"] > 700:
        return "MEDIUM", "Air quality reading is high"

    if data["humidity"] > 70:
        return "MEDIUM", "Humidity is high"

    if data["spo2"] < 96:
        return "MEDIUM", "SpO2 is slightly low"

    return "LOW", "All simulated readings are within the normal test range"


def generate_reading(timestamp):
    data = {
        "device_id": "child_001",
        "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
        "spo2": random.randint(92, 99),
        "heart_rate": random.randint(75, 125),
        "temperature": round(random.uniform(22.0, 30.0), 1),
        "humidity": round(random.uniform(40.0, 85.0), 1),
        "air_quality_raw": random.randint(250, 900),
    }

    risk_level, reason = calculate_risk(data)

    data["risk_level"] = risk_level
    data["reason"] = reason

    return data


def generate_dataset(number_of_readings=200):
    readings = []
    start_time = datetime.now()

    for i in range(number_of_readings):
        timestamp = start_time + timedelta(minutes=i * 5)
        readings.append(generate_reading(timestamp))

    return readings


def save_to_csv(readings, filename):
    fieldnames = [
        "device_id",
        "timestamp",
        "spo2",
        "heart_rate",
        "temperature",
        "humidity",
        "air_quality_raw",
        "risk_level",
        "reason",
    ]

    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(readings)


if __name__ == "__main__":
    dataset = generate_dataset(200)
    save_to_csv(dataset, "simulation/simulated_asthma_readings.csv")

    print("Generated simulation/simulated_asthma_readings.csv")
    print(f"Total readings: {len(dataset)}")