from pathlib import Path
import pandas as pd

RAW = Path("data/raw")

def profile_dataframe(df, filename):
    print(f"\n{'='*50}")
    print(f"PROFILING: {filename}")
    print(f"{'='*50}")
    
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print(f"\nColumn Names: {list(df.columns)}")
    print(f"\nData Types:")
    print(df.dtypes)
    print(f"\nNull Values:")
    print(df.isna().sum())
    print(f"\nDuplicate Rows: {df.duplicated().sum()}")
    print(f"\nFirst 5 Rows:")
    print(df.head())

try:
    customers = pd.read_csv(RAW / "customers.csv")
    profile_dataframe(customers, "customers.csv")
except Exception as e:
    print(f"Error reading customers.csv: {e}")

try:
    orders = pd.read_json(RAW / "orders.json")
    profile_dataframe(orders, "orders.json")
except Exception as e:
    print(f"Error reading orders.json: {e}")

try:
    products = pd.read_parquet(RAW / "products.parquet")
    profile_dataframe(products, "products.parquet")
except Exception as e:
    print(f"Error reading products.parquet: {e}")
    