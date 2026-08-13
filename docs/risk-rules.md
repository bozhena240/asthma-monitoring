# Risk Engine Rules

The current risk engine uses simulated values. These thresholds are temporary and are used only for software testing.

## Simulated Inputs

- SpO2: 92-99%
- Heart rate: 75-124 bpm
- Temperature: 22.0-29.9 C
- Humidity: 40-84%
- Air quality raw value: 250-899

## Risk Levels

### LOW

Assigned when all simulated readings are within the normal test range.

### MEDIUM

Assigned when one warning sign appears, such as:

- SpO2 below 96%
- Humidity above 70%
- Air quality raw value above 700

### HIGH

Assigned when SpO2 is below 94%, especially when combined with poor air quality.

## Medical Safety Note

These rules are not clinical recommendations. Final thresholds must be reviewed with medical literature and a qualified clinician before any real use.