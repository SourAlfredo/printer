import json
from pathlib import Path
import pandas as pd

script_path = Path(__file__).resolve()
script_dir = script_path.parent

json_path = Path(script_dir / "output_json.json")
csv_path = Path(script_dir / "output_csv.csv")

with open(json_path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)
df = pd.json_normalize(json_data)
df.to_csv(csv_path)
