# 🚌 BVG delay tracker
An automated data pipeline that analyzes public transportation delay data for Berlin (BVG), collected continuously over 16 days from a real-time API.

## 📡 Data Source

Departure and delay data is collected from the [VBB REST API](https://v6.vbb.transport.rest/getting-started.html), a community-built, open-source wrapper around Berlin's public transit real-time data (BVG/VBB network).

## 🛠️ Tools Used

- Python
- PowerBI

## 📁 Project Structure

- **collector/**: `collector.py` — fetches real-time departure data from the VBB API
- **.github/workflows/**: `collect.yml` — GitHub Actions workflow that runs the collector every 10 minutes
- **pipeline/**: contains 3 scripts
    - `parse_and_load.py` — parses raw JSON files, cleans and deduplicates records, and loads them into a SQLite database
    - `check_data.py` — runs SQL queries to validate and explore the cleaned data
    - `debug_modes.py` — used to inspect raw API fields during development
- **data/**: contains raw data, the database, and exported files
    - `raw/` — raw JSON snapshots collected every 10 minutes
    - `bvg_delays.db` — cleaned SQLite database
    - `departures_clean.csv` — exported dataset used for loading into Power BI
- **requirements.txt**: Python dependencies
- **Power BI Dashboard/**: contains `bvg_delay_tracker.pbix` (the Power BI dashboard file) and a screenshot of the dashboard


## 📊 Overview
- We have collected 52.50K data over 16 days for 3 stations in Berlin : Alexanderplatz, Hauptbahnhof, and Kottbusser Tor.
- After 16 days of data collecting for three stations of Berlin, we have figured out that departures from the Hauptbahnhof station have the highest delay average (24.65).
- Public transportation system in berlin contains suburban, buses, trams and subway.
- Ranked by average delay, suburban trains (S-Bahn) recorded the highest average delay(25.64), followed by buses(21.98), trams(19.35), and subway (U-Bahn) lines(11.81), which had the lowest and most consistent delays.
- We have 5 delay categories (Early, On time, Low Delay, Medium Delay and High Delay), and after analyzing we have figured out that 75.88% of departures are on time, 13% have a low delay of about 1-2 min, and only 1.44% have a high delay (more than 5 min).
- Top 5 most delayed lines, in order, are bus 147, bus N40, suburban S5, tram M10 and tram M8 with average delays of 68.10, 38.47, 41.79, 38.82, 38.86.

## ✍️ Author

Mahya
