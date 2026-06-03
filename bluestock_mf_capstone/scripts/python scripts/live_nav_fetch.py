import requests
import pandas as pd
from pathlib import Path

url = "https://api.mfapi.in/mf/125497"

try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    nav_df = pd.DataFrame(data["data"])

    output_file = "HDFC_Top100_Live_NAV.csv"

    nav_df.to_csv(output_file, index=False)

    print(f"Saved: {output_file}")

except requests.exceptions.Timeout:
    print("Request timed out")

except Exception as e:
    print("Error:", e)