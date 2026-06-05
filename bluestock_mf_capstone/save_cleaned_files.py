import pandas as pd
from pathlib import Path

# ==========================
# Create processed folder
# ==========================

processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)

# ==========================
# File Mapping
# ==========================

files = {
    "01_fund_master(2).csv": "fund_master_clean.csv",
    "02_nav_history(2).csv": "nav_history_clean.csv",
    "03_aum_by_fund_house(2).csv": "aum_clean.csv",
    "04_monthly_sip_inflows(2).csv": "monthly_sip_inflows_clean.csv",
    "05_category_inflows(2).csv": "category_inflows_clean.csv",
    "06_industry_folio_count(2).csv": "folio_count_clean.csv",
    "07_scheme_performance(2).csv": "scheme_performance_clean.csv",
    "08_investor_transactions(2).csv": "investor_transactions_clean.csv",
    "09_portfolio_holdings(2).csv": "portfolio_holdings_clean.csv",
    "10_benchmark_indices(2).csv": "benchmark_indices_clean.csv"
}

# ==========================
# Process Files
# ==========================

for source_file, target_file in files.items():

    try:
        df = pd.read_csv(source_file)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove completely empty rows
        df = df.dropna(how="all")

        output_path = processed_dir / target_file

        df.to_csv(
            output_path,
            index=False
        )

        print(f"✓ Saved: {output_path}")

    except FileNotFoundError:
        print(f"✗ File not found: {source_file}")

    except Exception as e:
        print(f"✗ Error processing {source_file}: {e}")

print("\nAll available files processed successfully.")