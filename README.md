# BVG delay tracker
An automated data pipeline that analyzes public transportation delay data for Berlin (BVG), collected continuously over 16 days from a real-time API.

## Data Source

Departure and delay data is collected from the [VBB REST API](https://v6.vbb.transport.rest/getting-started.html), a community-built, open-source wrapper around Berlin's public transit real-time data (BVG/VBB network).

## Tools Used
- Python
- PowerBI

## Project Structure

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
- **powerbi/**: contains `bvg_delay_tracker.pbix` (the Power BI dashboard file) and a screenshot of the dashboard
