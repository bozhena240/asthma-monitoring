import json
from pathlib import Path


def build_dashboard():
    input_file = Path("simulation/simulated_asthma_readings.json")
    output_dir = Path("dashboard")
    output_file = output_dir / "index.html"

    output_dir.mkdir(exist_ok=True)

    with open(input_file, "r") as file:
        data = json.load(file)

    readings = data["readings"]
    latest = readings[-1]

    risk_counts = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}

    for reading in readings:
        risk_counts[reading["riskLevel"]] += 1

    recent_alerts = [
        reading for reading in readings if reading["riskLevel"] in ["MEDIUM", "HIGH"]
    ][-10:]
    recent_alerts.reverse()

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Pediatric Asthma Monitoring Dashboard</title>
  <style>
    body {{
      font-family: Arial, sans-serif;
      margin: 0;
      background: #f4f7fb;
      color: #1f2937;
    }}

    header {{
      background: #0f766e;
      color: white;
      padding: 24px;
    }}

    main {{
      padding: 24px;
      max-width: 1100px;
      margin: auto;
    }}

    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}

    .card {{
      background: white;
      padding: 18px;
      border-radius: 8px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
    }}

    .label {{
      color: #64748b;
      font-size: 14px;
    }}

    .value {{
      font-size: 28px;
      font-weight: bold;
      margin-top: 8px;
    }}

    .risk-low {{
      color: #16a34a;
    }}

    .risk-medium {{
      color: #d97706;
    }}

    .risk-high {{
      color: #dc2626;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      background: white;
      border-radius: 8px;
      overflow: hidden;
    }}

    th, td {{
      padding: 12px;
      border-bottom: 1px solid #e5e7eb;
      text-align: left;
      font-size: 14px;
    }}

    th {{
      background: #e0f2f1;
    }}
  </style>
</head>
<body>
  <header>
    <h1>Pediatric Asthma Monitoring Dashboard</h1>
    <p>Simulation dashboard using generated sensor data.</p>
  </header>

  <main>
    <h2>Latest Reading</h2>

    <div class="grid">
      <div class="card">
        <div class="label">Risk Level</div>
        <div class="value risk-{latest["riskLevel"].lower()}">{latest["riskLevel"]}</div>
      </div>

      <div class="card">
        <div class="label">SpO2</div>
        <div class="value">{latest["spo2"]}%</div>
      </div>

      <div class="card">
        <div class="label">Heart Rate</div>
        <div class="value">{latest["heartRate"]} bpm</div>
      </div>

      <div class="card">
        <div class="label">Humidity</div>
        <div class="value">{latest["humidity"]}%</div>
      </div>

      <div class="card">
        <div class="label">Air Quality Raw</div>
        <div class="value">{latest["airQualityRaw"]}</div>
      </div>
    </div>

    <h2>Risk Summary</h2>

    <div class="grid">
      <div class="card">
        <div class="label">LOW</div>
        <div class="value risk-low">{risk_counts["LOW"]}</div>
      </div>

      <div class="card">
        <div class="label">MEDIUM</div>
        <div class="value risk-medium">{risk_counts["MEDIUM"]}</div>
      </div>

      <div class="card">
        <div class="label">HIGH</div>
        <div class="value risk-high">{risk_counts["HIGH"]}</div>
      </div>
    </div>

    <h2>Recent Alerts</h2>

    <table>
      <tr>
        <th>Time</th>
        <th>Risk</th>
        <th>SpO2</th>
        <th>Humidity</th>
        <th>Air Quality</th>
        <th>Reason</th>
      </tr>
"""

    for alert in recent_alerts:
        risk_class = alert["riskLevel"].lower()
        html += f"""
      <tr>
        <td>{alert["timestamp"]}</td>
        <td class="risk-{risk_class}">{alert["riskLevel"]}</td>
        <td>{alert["spo2"]}%</td>
        <td>{alert["humidity"]}%</td>
        <td>{alert["airQualityRaw"]}</td>
        <td>{alert["reason"]}</td>
      </tr>
"""

    html += """
    </table>
  </main>
</body>
</html>
"""

    with open(output_file, "w") as file:
        file.write(html)

    print(f"Created {output_file}")


if __name__ == "__main__":
    build_dashboard()