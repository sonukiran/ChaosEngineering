# app/database.py
import json
from pathlib import Path

data_file = Path("app/data.json")

# Initialize the JSON file if it doesn't exist
if not data_file.exists():
    data_file.write_text("[]")

# Helper function to read items from JSON
def read_items():
    with open(data_file, "r") as f:
        return json.load(f)

# Helper function to write items to JSON
def write_items(items):
    with open(data_file, "w") as f:
        json.dump(items, f, indent=4)
