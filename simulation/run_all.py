import subprocess
import sys

scripts = [
    "simulation/generate_dataset.py",
    "simulation/analyze_dataset.py",
    "simulation/export_to_json.py",
    "simulation/plot_dataset.py",
    "simulation/build_dashboard.py",
]

def run_script(script):
    print(f"\nRunning {script}")
    print("-" * 50)

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"Error while running {script}")
        sys.exit(result.returncode)


if __name__ == "__main__":
    print("Running full asthma monitoring simulation pipeline")

    for script in scripts:
        run_script(script)

    print("\nSimulation pipeline completed successfully.")
    print("Open dashboard/index.html to view the dashboard.")