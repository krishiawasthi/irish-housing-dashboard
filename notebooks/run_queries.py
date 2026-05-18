import sqlite3
import pandas as pd
import os

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create paths
db_path = os.path.join(BASE_DIR, "data", "processed", "housing.db")
county_csv = os.path.join(BASE_DIR, "data", "processed", "avg_by_county.csv")
trend_csv = os.path.join(BASE_DIR, "data", "processed", "trend_by_year.csv")

# Connect to database
conn = sqlite3.connect(db_path)

# Query 1 — average price by county
q1 = """
SELECT county,
       ROUND(AVG(price), 2) AS avg_price,
       COUNT(*) AS total_sales
FROM transactions
GROUP BY county
ORDER BY avg_price DESC
"""

result1 = pd.read_sql(q1, conn)

# Save CSV
result1.to_csv(county_csv, index=False)

print("Query 1 done:", result1.shape)

# Query 2 — yearly trend
q2 = """
SELECT year,
       ROUND(AVG(price), 2) AS avg_price,
       COUNT(*) AS total_sales
FROM transactions
GROUP BY year
ORDER BY year
"""

result2 = pd.read_sql(q2, conn)

# Save CSV
result2.to_csv(trend_csv, index=False)

print("Query 2 done:", result2.shape)

conn.close()

print("All queries complete.")