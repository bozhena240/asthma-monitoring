#include <Arduino.h>

struct SensorData {
  int spo2;
  int heartRate;
  float temperature;
  float humidity;
  int airQuality;
};

String calculateRisk(SensorData data) {
  if (data.spo2 < 94 && data.airQuality > 700) {
    return "HIGH";
  }

  if (data.spo2 < 96 || data.humidity > 70 || data.airQuality > 500) {
    return "MEDIUM";
  }

  return "LOW";
}

SensorData getSimulatedSensorData() {
  SensorData data;

  data.spo2 = random(92, 100);
  data.heartRate = random(75, 120);
  data.temperature = random(220, 290) / 10.0;
  data.humidity = random(45, 80);
  data.airQuality = random(250, 850);

  return data;
}

void printSensorData(SensorData data, String riskLevel) {
  Serial.println("----- Asthma Monitor Reading -----");
  Serial.print("SpO2: ");
  Serial.print(data.spo2);
  Serial.println("%");

  Serial.print("Heart Rate: ");
  Serial.print(data.heartRate);
  Serial.println(" bpm");

  Serial.print("Temperature: ");
  Serial.print(data.temperature);
  Serial.println(" C");

  Serial.print("Humidity: ");
  Serial.print(data.humidity);
  Serial.println("%");

  Serial.print("Air Quality: ");
  Serial.println(data.airQuality);

  Serial.print("Risk Level: ");
  Serial.println(riskLevel);
  Serial.println();
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  randomSeed(analogRead(0));

  Serial.println("Pediatric Asthma Monitoring System Started");
  Serial.println("Using simulated sensor values for now.");
  Serial.println();
}

void loop() {
  SensorData currentData = getSimulatedSensorData();
  String riskLevel = calculateRisk(currentData);

  printSensorData(currentData, riskLevel);

  delay(3000);
}