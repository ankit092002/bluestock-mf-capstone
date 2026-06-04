import pandas as pd
from pathlib import Path

# Current project folder
BASE_DIR = Path(__file__).resolve().parent

# Find the NAV file automatically
csv_files = list(BASE_DIR.rglob("*02*nav*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "Could not find 02_nav_history.csv anywhere in the project."
    )

file_path = csv_files[0]

print(f"Reading: {file_path}")

# Load CSV
nav = pd.read_csv(file_path)

print("Columns:")
print(nav.columns.tolist())

print("Original Shape:", nav.shape)

# -----------------------
# Adjust column names if needed
# -----------------------

# Example expected columns:
# amfi_code, date, nav

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav = nav.dropna(subset=["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = (
    nav.groupby("amfi_code")["nav"]
    .ffill()
)

nav = nav.drop_duplicates()

nav = nav[
    (nav["nav"] > 0)
    & (nav["nav"].notna())
]

# Create processed folder
processed_dir = BASE_DIR / "data" / "processed"
processed_dir.mkdir(parents=True, exist_ok=True)

output_file = processed_dir / "nav_history_clean.csv"

nav.to_csv(
    output_file,
    index=False
)

print("Cleaned Shape:", nav.shape)
print(f"Saved: {output_file}")

# ======================================
# Locate investor_transactions file
# ======================================

BASE_DIR = Path(__file__).resolve().parent

csv_files = list(BASE_DIR.rglob("*08*investor*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "08_investor_transactions.csv not found in project folders."
    )

file_path = csv_files[0]

print(f"Reading file: {file_path}")

# ======================================
# Load Data
# ======================================

txn = pd.read_csv(file_path)

print("\nColumns:")
print(txn.columns.tolist())

print("\nOriginal Shape:")
print(txn.shape)

# ======================================
# Convert Date
# ======================================

if "transaction_date" in txn.columns:
    txn["transaction_date"] = pd.to_datetime(
        txn["transaction_date"],
        errors="coerce"
    )

    txn = txn.dropna(
        subset=["transaction_date"]
    )

# ======================================
# Standardize Transaction Types
# ======================================

if "transaction_type" in txn.columns:

    txn["transaction_type"] = (
        txn["transaction_type"]
        .astype(str)
        .str.strip()
        .str.lower()
    )

    mapping = {
        "sip": "SIP",
        "systematic investment plan": "SIP",
        "lumpsum": "Lumpsum",
        "lump sum": "Lumpsum",
        "purchase": "Lumpsum",
        "redeem": "Redemption",
        "redemption": "Redemption",
        "withdrawal": "Redemption"
    }

    txn["transaction_type"] = (
        txn["transaction_type"]
        .replace(mapping)
    )

# ======================================
# Validate Amount
# ======================================

if "amount" in txn.columns:

    txn["amount"] = pd.to_numeric(
        txn["amount"],
        errors="coerce"
    )

    txn = txn[
        (txn["amount"] > 0)
    ]

# ======================================
# Validate KYC Status
# ======================================

if "kyc_status" in txn.columns:

    txn["kyc_status"] = (
        txn["kyc_status"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    valid_kyc = [
        "Verified",
        "Pending",
        "Rejected"
    ]

    txn["kyc_valid"] = (
        txn["kyc_status"]
        .isin(valid_kyc)
    )

# ======================================
# Remove Duplicates
# ======================================

txn = txn.drop_duplicates()

print("\nCleaned Shape:")
print(txn.shape)

# ======================================
# Save Cleaned File
# ======================================

processed_dir = (
    BASE_DIR /
    "data" /
    "processed"
)

processed_dir.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    processed_dir /
    "investor_transactions_clean.csv"
)

txn.to_csv(
    output_file,
    index=False
)

print(f"\nSaved Successfully:")
print(output_file)

print("\nCleaning Completed.")


# ======================================
# Locate scheme_performance file
# ======================================

BASE_DIR = Path(__file__).resolve().parent

csv_files = list(BASE_DIR.rglob("*07*scheme*performance*.csv"))

if not csv_files:
    raise FileNotFoundError(
        "07_scheme_performance.csv not found in project folders."
    )

file_path = csv_files[0]

print(f"Reading file: {file_path}")

# ======================================
# Load Data
# ======================================

perf = pd.read_csv(file_path)

print("\nColumns:")
print(perf.columns.tolist())

print("\nOriginal Shape:")
print(perf.shape)

# ======================================
# Convert Return Columns to Numeric
# ======================================

return_columns = [
    col for col in perf.columns
    if "return" in col.lower()
]

for col in return_columns:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# ======================================
# Flag Return Anomalies
# ======================================

perf["return_anomaly"] = False

for col in return_columns:
    perf["return_anomaly"] = (
        perf["return_anomaly"] |
        (perf[col] > 100) |
        (perf[col] < -50)
    )

# ======================================
# Expense Ratio Validation
# ======================================

expense_cols = [
    col for col in perf.columns
    if "expense" in col.lower()
]

if expense_cols:

    expense_col = expense_cols[0]

    perf[expense_col] = pd.to_numeric(
        perf[expense_col],
        errors="coerce"
    )

    perf["expense_ratio_valid"] = (
        perf[expense_col]
        .between(0.1, 2.5)
    )

# ======================================
# Remove Duplicates
# ======================================

perf = perf.drop_duplicates()

# ======================================
# Missing Values Report
# ======================================

print("\nMissing Values:")

print(
    perf.isnull()
    .sum()
)

print("\nCleaned Shape:")
print(perf.shape)

# ======================================
# Save Cleaned File
# ======================================

processed_dir = (
    BASE_DIR /
    "data" /
    "processed"
)

processed_dir.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    processed_dir /
    "scheme_performance_clean.csv"
)

perf.to_csv(
    output_file,
    index=False
)

print(f"\nSaved Successfully:")
print(output_file)

print("\nCleaning Completed.")