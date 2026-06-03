import pandas as pd
from pathlib import Path

# Path to data/raw folder
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    print("=" * 80)
    print(f"Dataset: {file}")

    file_path = DATA_PATH / file

    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue

    df = pd.read_csv(file_path)

    print("Shape:")
    print(df.shape)

    print("Data Types:")
    print(df.dtypes)

    print("First 5 Rows:")
    print(df.head())

    print(" ")