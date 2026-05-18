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