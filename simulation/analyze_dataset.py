import csv
from collections import Counter


def analyze_dataset(filename):
    risk_counts = Counter()
    total_readings = 0

    spo2_values = []
    heart_rate_values = []
    humidity_values = []
    air_quality_values = []

    with open(filename, "r") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            total_readings += 1

            risk_counts[row["risk_level"]] += 1

            spo2_values.append(int(row["spo2"]))
            heart_rate_values.append(int(row["heart_rate"]))
            humidity_values.append(float(row["humidity"]))
            air_quality_values.append(int(row["air_quality_raw"]))

    print("Asthma Monitoring Dataset Analysis")
    print("-" * 50)
    print(f"Total readings: {total_readings}")
    print()

    print("Risk level counts:")
    for risk_level, count in risk_counts.items():
        percentage = (count / total_readings) * 100
        print(f"{risk_level}: {count} readings ({percentage:.1f}%)")

    print()
    print("Sensor value ranges:")
    print(f"SpO2: {min(spo2_values)}% - {max(spo2_values)}%")
    print(f"Heart rate: {min(heart_rate_values)} - {max(heart_rate_values)} bpm")
    print(f"Humidity: {min(humidity_values)}% - {max(humidity_values)}%")
    print(f"Air quality raw: {min(air_quality_values)} - {max(air_quality_values)}")


if __name__ == "__main__":
    analyze_dataset("simulation/simulated_asthma_readings.csv")