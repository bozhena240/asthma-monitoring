#include <Arduino.h>

struct SensorData {
  const char* deviceId;
  int spo2;
  int heartRate;
  float temperature;
  float humidity;
  int airQualityRaw;
};

struct RiskResult {
  const char* level;
  const char* reason;
};

SensorData getSimulatedSensorData() {
  SensorData data;

  data.deviceId = "child_001";
  data.spo2 = random(92, 100);
  data.heartRate = random(75, 125);
  data.temperature = random(220, 300) / 10.0;
  data.humidity = random(40, 85);
  data.airQualityRaw = random(250, 900);

  return data;
}

RiskResult calculateRisk(SensorData data) {
  RiskResult result;

  if (data.spo2 < 94 && data.airQualityRaw > 700) {
    result.level = "HIGH";
    result.reason = "Low SpO2 combined with poor air quality";
    return result;
  }

  if (data.spo2 < 94) {
    result.level = "HIGH";
    result.reason = "SpO2 is below the safety threshold";
    return result;
  }

  if (data.airQualityRaw > 700) {
    result.level = "MEDIUM";
    result.reason = "Air quality reading is high";
    return result;
  }

  if (data.humidity > 70) {
    result.level = "MEDIUM";
    result.reason = "Humidity is high";
    return result;
  }

  if (data.spo2 < 96) {
    result.level = "MEDIUM";
    result.reason = "SpO2 is slightly low";
    return result;
  }

  result.level = "LOW";
  result.reason = "All simulated readings are within the normal test range";
  return result;
}

void printJsonReading(SensorData data, RiskResult risk) {
  Serial.println("{");

  Serial.print("  \"deviceId\": \"");
  Serial.print(data.deviceId);
  Serial.println("\",");

  Serial.print("  \"spo2\": ");
  Serial.print(data.spo2);
  Serial.println(",");

  Serial.print("  \"heartRate\": ");
  Serial.print(data.heartRate);
  Serial.println(",");

  Serial.print("  \"temperature\": ");
  Serial.print(data.temperature, 1);
  Serial.println(",");

  Serial.print("  \"humidity\": ");
  Serial.print(data.humidity, 1);
  Serial.println(",");

  Serial.print("  \"airQualityRaw\": ");
  Serial.print(data.airQualityRaw);
  Serial.println(",");

  Serial.print("  \"riskLevel\": \"");
  Serial.print(risk.level);
  Serial.println("\",");

  Serial.print("  \"reason\": \"");
  Serial.print(risk.reason);
  Serial.println("\"");

  Serial.println("}");
  Serial.println();
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  randomSeed(analogRead(0));

  Serial.println("Pediatric Asthma Monitoring Simulation Started");
  Serial.println("Generating JSON-style simulated sensor readings.");
  Serial.println();
}

void loop() {
  SensorData currentData = getSimulatedSensorData();
  RiskResult risk = calculateRisk(currentData);

  printJsonReading(currentData, risk);

  delay(3000);
}