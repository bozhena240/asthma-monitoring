import csv
import json


def csv_to_json(csv_filename, json_filename):
    readings = []

    with open(csv_filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            reading = {
                "deviceId": row["device_id"],
                "timestamp": row["timestamp"],
                "spo2": int(row["spo2"]),
                "heartRate": int(row["heart_rate"]),
                "temperature": float(row["temperature"]),
                "humidity": float(row["humidity"]),
                "airQualityRaw": int(row["air_quality_raw"]),
                "riskLevel": row["risk_level"],
                "reason": row["reason"],
            }

            readings.append(reading)

    data = {
        "deviceId": "child_001",
        "readings": readings,
    }

    with open(json_filename, "w") as jsonfile:
        json.dump(data, jsonfile, indent=2)

    print(f"Exported {len(readings)} readings to {json_filename}")


if __name__ == "__main__":
    csv_to_json(
        "simulation/simulated_asthma_readings.csv",
        "simulation/simulated_asthma_readings.json",
    )