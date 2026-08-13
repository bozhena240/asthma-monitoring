test_scenarios = [
    {
        "scenario": "NORMAL",
        "spo2": 98,
        "heart_rate": 88,
        "temperature": 24.5,
        "humidity": 52.0,
        "air_quality_raw": 320,
        "expected_risk": "LOW",
    },
    {
        "scenario": "HUMIDITY_WARNING",
        "spo2": 97,
        "heart_rate": 90,
        "temperature": 25.0,
        "humidity": 76.0,
        "air_quality_raw": 350,
        "expected_risk": "MEDIUM",
    },
    {
        "scenario": "AIR_QUALITY_WARNING",
        "spo2": 97,
        "heart_rate": 92,
        "temperature": 24.8,
        "humidity": 55.0,
        "air_quality_raw": 760,
        "expected_risk": "MEDIUM",
    },
    {
        "scenario": "LOW_SPO2",
        "spo2": 93,
        "heart_rate": 105,
        "temperature": 24.7,
        "humidity": 58.0,
        "air_quality_raw": 400,
        "expected_risk": "HIGH",
    },
    {
        "scenario": "HIGH_RISK_COMBINED",
        "spo2": 92,
        "heart_rate": 118,
        "temperature": 25.3,
        "humidity": 72.0,
        "air_quality_raw": 820,
        "expected_risk": "HIGH",
    },
]


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


def run_simulation():
    print("Pediatric Asthma Monitoring Python Simulation")
    print("-" * 60)

    passed_count = 0

    for data in test_scenarios:
        actual_risk, reason = calculate_risk(data)
        passed = actual_risk == data["expected_risk"]

        if passed:
            passed_count += 1

        print(f"Scenario: {data['scenario']}")
        print(f"Expected Risk: {data['expected_risk']}")
        print(f"Actual Risk: {actual_risk}")
        print(f"Reason: {reason}")
        print(f"Test Passed: {passed}")
        print("-" * 60)

    print(f"Passed {passed_count} out of {len(test_scenarios)} tests.")


if __name__ == "__main__":
    run_simulation()