import pandas as pd
from pathlib import Path

# Project root folder
BASE_DIR = Path(__file__).resolve().parent

# File path
file_path = BASE_DIR / "data" / "raw" / "01_fund_master.csv"

print("=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

print("\nFile Location:")
print(file_path)

# Check file exists
if not file_path.exists():
    print("\nERROR: File not found!")
    print("Expected location:", file_path)
    exit()

# Load dataset
df = pd.read_csv(file_path)

# Dataset shape
print("\nDataset Shape:")
print(df.shape)

# Columns
print("\nColumns:")
print(df.columns.tolist())

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Unique Fund Houses
if "fund_house" in df.columns:
    print("\nUnique Fund Houses:")
    print(df["fund_house"].unique())

    print("\nNumber of Fund Houses:")
    print(df["fund_house"].nunique())

# Categories
if "category" in df.columns:
    print("\nCategories:")
    print(df["category"].unique())

    print("\nFunds per Category:")
    print(df["category"].value_counts())

# Sub Categories
if "sub_category" in df.columns:
    print("\nSub Categories:")
    print(df["sub_category"].unique())

# Risk Categories
if "risk_category" in df.columns:
    print("\nRisk Categories:")
    print(df["risk_category"].unique())

    print("\nFunds per Risk Category:")
    print(df["risk_category"].value_counts())

# AMFI Codes
if "amfi_code" in df.columns:
    print("\nSample AMFI Codes:")
    print(df["amfi_code"].head(10))

    print("\nTotal Unique AMFI Codes:")
    print(df["amfi_code"].nunique())

print("\n" + "=" * 80)
print("FUND MASTER ANALYSIS COMPLETED")
print("=" * 80)