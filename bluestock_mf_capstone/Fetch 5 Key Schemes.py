import requests
import pandas as pd
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent

# Create data/raw folder if it doesn't exist
raw_folder = BASE_DIR / "data" / "raw"
raw_folder.mkdir(parents=True, exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():

    try:
        url = f"https://api.mfapi.in/mf/{code}"

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = raw_folder / f"{name}.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"✅ {name} downloaded successfully")

    except Exception as e:
        print(f"❌ Error downloading {name}: {e}")