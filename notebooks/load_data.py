<<<<<<< HEAD
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
=======
import pandas as pd      # pandas = tool for reading and editing data tables
import os

os.makedirs("../data/processed", exist_ok=True)
import sqlite3           # sqlite3 = tool for creating a simple local database

# Step 1: Read the CSV file into Python
# pd.read_csv reads the file and creates a "dataframe" (like a spreadsheet in Python)
df = pd.read_csv("/Users/krishiawasthi/Desktop/irish-housing-dashboard/data/data.csv")

# Step 2: Print the first 5 rows so you can see what the data looks like
print(df.head())

# Step 3: Print the column names so you know what to work with
print(df.columns.tolist())

# Step 4: Clean the data — rename columns to simple names
df.columns = [
    "date",
    "address",
    "county",
    "eircode",
    "price",
    "not_full_price",
    "vat_exclusive",
    "property_description",
    "property_size"
]

# Step 5: Remove the euro sign from the price column and convert to a number
df["price"] = df["price"].str.replace("€", "").str.replace(",", "").astype(float)

# Step 6: Convert the date column to a proper date format
df["date"] = pd.to_datetime(
    df["date"],
    format="%d/%m/%Y",
    errors="coerce"
)

# Step 7: Add a "year" column by extracting just the year from the date
df["year"] = df["date"].dt.year

# Step 8: Connect to (or create) a SQLite database file
# This creates a file called housing.db in your data/processed folder
conn = sqlite3.connect("../data/processed/housing.db")

# Step 9: Write the cleaned dataframe into the database as a table called "transactions"
# if_exists="replace" means: if the table already exists, overwrite it
df.to_sql("transactions", conn, if_exists="replace", index=False)

# Step 10: Confirm it worked
print("Data loaded successfully! Rows:", len(df))
conn.close()
>>>>>>> 9615b6eb1df91d666e09a27a0160fbf6acbc7196
