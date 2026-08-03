import requests
import json
import os
from datetime import datetime, timezone

STATIONS = {
    "alexanderplatz": "900100003",
    "hauptbahnhof": "900003201",
    "kottbusser_tor": "900013102",
}

OUTPUT_DIR = "data/raw"

def fetch_departures(station_id):
    url = f"https://v6.vbb.transport.rest/stops/{station_id}/departures"
    resp = requests.get(url, params={"duration": 30}, timeout=10)
    resp.raise_for_status()
    return resp.json()

def save_raw(station_name, data):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
    path = f"{OUTPUT_DIR}/{station_name}_{ts}.json"
    with open(path, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    for name, sid in STATIONS.items():
        try:
            data = fetch_departures(sid)
            save_raw(name, data)
        except Exception as e:
            print(f"Failed for {name}: {e}")
