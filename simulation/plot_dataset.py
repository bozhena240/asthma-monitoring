import csv
from collections import Counter
from datetime import datetime

import matplotlib.pyplot as plt


def load_dataset(filename):
    timestamps = []
    spo2_values = []
    heart_rate_values = []
    humidity_values = []
    air_quality_values = []
    risk_levels = []

    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            timestamps.append(datetime.fromisoformat(row["timestamp"]))
            spo2_values.append(int(row["spo2"]))
            heart_rate_values.append(int(row["heart_rate"]))
            humidity_values.append(float(row["humidity"]))
            air_quality_values.append(int(row["air_quality_raw"]))
            risk_levels.append(row["risk_level"])

    return {
        "timestamps": timestamps,
        "spo2": spo2_values,
        "heart_rate": heart_rate_values,
        "humidity": humidity_values,
        "air_quality": air_quality_values,
        "risk_levels": risk_levels,
    }


def plot_risk_distribution(risk_levels):
    counts = Counter(risk_levels)

    plt.figure(figsize=(6, 4))
    plt.bar(counts.keys(), counts.values())
    plt.title("Risk Level Distribution")
    plt.xlabel("Risk Level")
    plt.ylabel("Number of Readings")
    plt.tight_layout()
    plt.savefig("simulation/risk_distribution.png")
    plt.close()


def plot_sensor_trends(data):
    timestamps = data["timestamps"]

    plt.figure(figsize=(10, 8))

    plt.subplot(3, 1, 1)
    plt.plot(timestamps, data["spo2"])
    plt.title("SpO2 Over Time")
    plt.ylabel("SpO2 (%)")

    plt.subplot(3, 1, 2)
    plt.plot(timestamps, data["humidity"])
    plt.title("Humidity Over Time")
    plt.ylabel("Humidity (%)")

    plt.subplot(3, 1, 3)
    plt.plot(timestamps, data["air_quality"])
    plt.title("Air Quality Raw Value Over Time")
    plt.ylabel("Raw Value")
    plt.xlabel("Time")

    plt.tight_layout()
    plt.savefig("simulation/sensor_trends.png")
    plt.close()


if __name__ == "__main__":
    dataset = load_dataset("simulation/simulated_asthma_readings.csv")

    plot_risk_distribution(dataset["risk_levels"])
    plot_sensor_trends(dataset)

    print("Created simulation/risk_distribution.png")
    print("Created simulation/sensor_trends.png")