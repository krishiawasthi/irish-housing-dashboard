import pandas as pd
import sqlite3
import os

# ── Paths ─────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "property_price_register.csv")
DB_PATH   = os.path.join(BASE_DIR, "data", "processed", "housing.db")

os.makedirs(os.path.join(BASE_DIR, "data", "processed"), exist_ok=True)

# ── Step 1: Load CSV ──────────────────────────────────────────────────
print("Loading data...")
df = pd.read_csv(DATA_PATH, low_memory=False)
print(f"Loaded {len(df):,} rows")

# ── Step 2: Parse dates ───────────────────────────────────────────────
df["date_of_sale"] = pd.to_datetime(df["date_of_sale"], dayfirst=True, errors="coerce")
df = df.dropna(subset=["date_of_sale"])

df["year"]    = df["date_of_sale"].dt.year
df["month"]   = df["date_of_sale"].dt.month
df["quarter"] = df["date_of_sale"].dt.quarter

# ── Step 3: Clean price ───────────────────────────────────────────────
df["price_eur"] = pd.to_numeric(df["price_eur"], errors="coerce")
df = df[(df["price_eur"] >= 10_000) & (df["price_eur"] <= 20_000_000)]

# ── Step 4: Clean county ──────────────────────────────────────────────
df["county"] = df["county"].str.strip().str.title()

# ── Step 5: New vs second-hand flag ──────────────────────────────────
df["is_new"]    = df["vat_exclusive"].astype(str).str.lower() == "true"
df["is_dublin"] = df["county"].str.lower() == "dublin"

# ── Step 6: Clean description ─────────────────────────────────────────
df["description"] = df["description"].str.strip()

print(f"Clean rows:  {len(df):,}")
print(f"Date range:  {df['date_of_sale'].min().date()} to {df['date_of_sale'].max().date()}")
print(f"Counties:    {df['county'].nunique()}")
print(f"Years:       {sorted(df['year'].unique().tolist())}")
print(f"Price range: €{df['price_eur'].min():,.0f} to €{df['price_eur'].max():,.0f}")

# ── Step 7: Save to SQLite ────────────────────────────────────────────
print("\nSaving to database...")
conn = sqlite3.connect(DB_PATH)
df.to_sql("transactions", conn, if_exists="replace", index=False)
conn.close()

print(f"Database saved to: {DB_PATH}")
print("Run run_queries.py next.")