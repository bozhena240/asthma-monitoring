# Pediatric Asthma Monitoring System

This project is an ESP32-based pediatric asthma monitoring prototype.

The system is designed to combine simulated physiological and environmental readings, including SpO2, heart rate, temperature, humidity, and air-quality values. A rule-based risk engine classifies each reading as LOW, MEDIUM, or HIGH risk.

At this stage, the project uses simulated sensor values only. Real physical sensors will be integrated later.

## Current Stage

- PlatformIO project created
- ESP32 Arduino framework selected
- Simulated sensor readings implemented
- JSON-style serial output implemented
- Basic rule-based risk engine implemented

## Planned Hardware

- ESP32 development board
- MAX30102 SpO2 and heart-rate sensor
- DHT22 temperature and humidity sensor
- Air-quality sensor
- Breadboard and jumper wires

## Important Note

This project is not a medical diagnostic device. It is an early-warning support prototype for educational and research purposes.

## How to Run the Simulation

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the full simulation pipeline:

```bash
python3 simulation/run_all.py
```

This will generate:

- simulated CSV readings
- dataset analysis output
- Firebase-style JSON data
- plot images
- local HTML dashboard

Open the dashboard:

```bash
open dashboard/index.html
```