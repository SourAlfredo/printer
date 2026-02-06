import csv
import json
from pathlib import Path

script_path = Path(__file__).resolve()
script_dir = script_path.parent

csv_path = Path(script_dir / "input.csv")
json_path = Path(script_dir / "outpot.json")

out = []
with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)  # uses the header row
    for row in reader:
        out.append(row)

with json_path.open("w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(out)} data to {json_path}")
