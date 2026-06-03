import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\nMissing Values:")
print(df.isnull().sum())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nFirst 5 Rows:")    
print(df.head())