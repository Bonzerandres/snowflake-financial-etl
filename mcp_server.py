import yaml
import subprocess
import sys
from pathlib import Path

PIPELINE_FILE = Path("mcp/workflows/fred_pipeline.yaml")

def load_pipelines():
    if not PIPELINE_FILE.exists():
        print("❌ No pipeline file found at mcp/workflows/fred_pipeline.yaml")
        sys.exit(1)
    with open(PIPELINE_FILE, "r") as f:
        return yaml.safe_load(f).get("pipelines", [])

def list_pipelines(pipelines):
    print("\n✅ Available Pipelines:")
    for p in pipelines:
        print(f" - {p['name']}: {p.get('description', '')}")
    print()

def run_pipeline(pipelines, name):
    pipeline = next((p for p in pipelines if p["name"] == name), None)
    if not pipeline:
        print(f"❌ Pipeline '{name}' not found.")
        sys.exit(1)
    cmd = pipeline["run"]
    
    print(f"🚀 Running pipeline: {name}")
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running pipeline: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python mcp_server.py [list | run <pipeline_name>]")
        sys.exit(0)

    command = sys.argv[1]
    pipelines = load_pipelines()

    if command == "list":
        list_pipelines(pipelines)
    elif command == "run" and len(sys.argv) == 3:
        run_pipeline(pipelines, sys.argv[2])
    else:
        print("Invalid command or missing pipeline name.")

if __name__ == "__main__":
    main()
