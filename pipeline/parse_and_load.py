import json
import glob
import sqlite3
import pandas as pd
import os


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
DB_PATH = os.path.join(PROJECT_ROOT, "data", "bvg_delays.db")
def load_all_raw_files():
    records = []
    files = glob.glob(f"{RAW_DIR}/*.json")
    print(f"Found {len(files)} raw files")

    for filepath in files:
        filename = filepath.replace("\\", "/").split("/")[-1]
        station_from_filename = filename.split("_")[0]

        with open(filepath, "r") as f:
            data = json.load(f)

        for dep in data.get("departures", []):
            product = dep.get("line", {}).get("product")
            if product not in ["subway", "tram", "bus", "suburban"]:
                continue
            records.append({
                "station": station_from_filename,
                "line": dep.get("line", {}).get("name"),
                "product": dep.get("line", {}).get("product"),
                "direction": dep.get("direction"),
                "trip_id": dep.get("tripId"),
                "planned_when": dep.get("plannedWhen"),
                "actual_when": dep.get("when"),
                "delay_seconds": dep.get("delay"),
            })

    return records

def main():
    records = load_all_raw_files()
    df = pd.DataFrame(records)
    print(f"Total records before dedup: {len(df)}")

    df = df.drop_duplicates(subset=["trip_id", "planned_when", "station"])
    print(f"Total records after dedup: {len(df)}")

    df = df.dropna(subset=["delay_seconds"])

    conn = sqlite3.connect(DB_PATH)
    df.to_sql("departures", conn, if_exists="replace", index=False)
    conn.close()

    print(f"Loaded {len(df)} clean records into {DB_PATH}")

if __name__ == "__main__":
    main()