#include <Arduino.h>

struct SensorData {
  const char* deviceId;
  const char* scenario;
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

SensorData testScenarios[] = {
  {"child_001", "NORMAL", 98, 88, 24.5, 52.0, 320},
  {"child_001", "HUMIDITY_WARNING", 97, 90, 25.0, 76.0, 350},
  {"child_001", "AIR_QUALITY_WARNING", 97, 92, 24.8, 55.0, 760},
  {"child_001", "LOW_SPO2", 93, 105, 24.7, 58.0, 400},
  {"child_001", "HIGH_RISK_COMBINED", 92, 118, 25.3, 72.0, 820}
};

int currentScenarioIndex = 0;
const int scenarioCount = sizeof(testScenarios) / sizeof(testScenarios[0]);

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

SensorData getNextScenario() {
  SensorData data = testScenarios[currentScenarioIndex];

  currentScenarioIndex++;

  if (currentScenarioIndex >= scenarioCount) {
    currentScenarioIndex = 0;
  }

  return data;
}

void printJsonReading(SensorData data, RiskResult risk) {
  Serial.println("{");

  Serial.print("  \"deviceId\": \"");
  Serial.print(data.deviceId);
  Serial.println("\",");

  Serial.print("  \"scenario\": \"");
  Serial.print(data.scenario);
  Serial.println("\",");

  Serial.print("  \"timestampMs\": ");
  Serial.print(millis());
  Serial.println(",");

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

  Serial.println("Pediatric Asthma Monitoring Simulation Started");
  Serial.println("Simulation 3: rotating through fixed test scenarios.");
  Serial.println();
}

void loop() {
  SensorData currentData = getNextScenario();
  RiskResult risk = calculateRisk(currentData);

  printJsonReading(currentData, risk);

  delay(3000);
}