import json
import glob
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")

files = glob.glob(f"{RAW_DIR}/*.json")

count = 0
for filepath in files[:20]:
    with open(filepath, "r") as f:
        data = json.load(f)
    for dep in data.get("departures", []):
        line = dep.get("line", {})
        if line.get("mode") == "train":
            print(line)
            count += 1
            if count >= 15:
                break
    if count >= 15:
        break