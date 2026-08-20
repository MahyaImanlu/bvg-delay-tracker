import sqlite3
import pandas as pd
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
DB_PATH = os.path.join(PROJECT_ROOT, "data", "bvg_delays.db")
CSV_PATH = os.path.join(PROJECT_ROOT, "data", "departures_clean.csv")
conn = sqlite3.connect(DB_PATH)

query = """
SELECT station, line, product, direction, planned_when, actual_when, delay_seconds
FROM departures;
"""

df = pd.read_sql(query, conn)
print(df.head())

conn.close()

df.to_csv(CSV_PATH, index=False)
print(f'{len(df)} rows exported to {CSV_PATH}')
