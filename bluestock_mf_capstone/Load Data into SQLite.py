from sqlalchemy import create_engine
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

engine = create_engine("sqlite:///bluestock_mf.db")

csv_files = list(BASE_DIR.rglob("*clean.csv"))

if not csv_files:
    raise FileNotFoundError(
        "No cleaned CSV files found."
    )

for file in csv_files:

    table_name = file.stem.replace("_clean", "")

    print(f"Loading {file.name} -> {table_name}")

    df = pd.read_csv(file)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Rows Loaded: {len(df)}")

print("All files loaded successfully.")




engine = create_engine("sqlite:///bluestock_mf.db")

tables = pd.read_sql("""
SELECT name
FROM sqlite_master
WHERE type='table'
""", engine)

print("\nTables Found:\n")
print(tables)

for table in tables["name"]:
    try:
        count = pd.read_sql(
            f"SELECT COUNT(*) AS row_count FROM '{table}'",
            engine
        )

        print(f"\n{table}")
        print(count)

    except Exception as e:
        print(f"Error in {table}: {e}")