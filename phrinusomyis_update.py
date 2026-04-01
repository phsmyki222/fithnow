import json

updates_file = "phrinusomyis_update.py"

with open(updates_file, "r", encoding="utf-8") as f:
    updates = json.load(f)   # instead of py.load(f)
