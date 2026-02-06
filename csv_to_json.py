import csv
import json
from pathlib import Path

csv_path = Path("C:/path/input.csv")
json_path = Path("C:/path/outpot.json")

out = []
with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)  # uses the header row
    for row in reader:
        out.append(
            {
                "columnA": (row.get("columnA") or "").strip(),
                "columnB": (row.get("columnB") or "").strip(),
                "columnC": (row.get("columnC") or "").strip(),
            }
        )

with json_path.open("w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(out)} data to {json_path}")
