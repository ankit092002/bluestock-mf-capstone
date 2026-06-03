import pandas as pd
from pathlib import Path

# Project root
BASE_DIR = Path(__file__).resolve().parent

# File paths
fund_master_file = BASE_DIR / "data" / "raw" / "01_fund_master.csv"
nav_history_file = BASE_DIR / "data" / "raw" / "02_nav_history.csv"

print("=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

# Check files exist
if not fund_master_file.exists():
    print("File not found: {fund_master_file}")
    exit()

if not nav_history_file.exists():
    print("File not found: {nav_history_file}")
    exit()

# Load data
fund_master = pd.read_csv(fund_master_file)
nav_history = pd.read_csv(nav_history_file)

# Convert to string
fund_master["amfi_code"] = fund_master["amfi_code"].astype(str)
nav_history["amfi_code"] = nav_history["amfi_code"].astype(str)

# Unique codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Missing codes
missing_codes = master_codes - nav_codes

print(f"Total Fund Master Codes : {len(master_codes)}")
print(f"Total NAV History Codes : {len(nav_codes)}")
print(f"Missing Codes           : {len(missing_codes)}")

if missing_codes:
    print("\nMissing AMFI Codes:")
    for code in sorted(missing_codes):
        print(code)
else:
    print("All AMFI codes exist in nav_history.csv")

# Duplicate check
print("Duplicate AMFI Codes in fund_master:")
print(fund_master["amfi_code"].duplicated().sum())

print("Duplicate AMFI Codes in nav_history:")
print(nav_history["amfi_code"].duplicated().sum())

print(" " + "=" * 80)
print("VALIDATION COMPLETED")
print("=" * 80)