import sqlite3
import pandas as pd
import os

<<<<<<< HEAD
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH  = os.path.join(BASE_DIR, "data", "processed", "housing.db")
OUT_DIR  = os.path.join(BASE_DIR, "data", "processed")

conn = sqlite3.connect(DB_PATH)

# ── Query 1: Average price by county ─────────────────────────────────
q1 = """
SELECT county,
       ROUND(AVG(price_eur), 0)  AS avg_price,
       ROUND(MIN(price_eur), 0)  AS min_price,
       ROUND(MAX(price_eur), 0)  AS max_price,
       COUNT(*)                  AS total_sales
=======
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
>>>>>>> 9615b6eb1df91d666e09a27a0160fbf6acbc7196
FROM transactions
GROUP BY county
ORDER BY avg_price DESC
"""
<<<<<<< HEAD
pd.read_sql(q1, conn).to_csv(f"{OUT_DIR}/avg_by_county.csv", index=False)
print("Query 1 done: avg by county")

# ── Query 2: Yearly trend ─────────────────────────────────────────────
q2 = """
SELECT year,
       ROUND(AVG(price_eur), 0) AS avg_price,
       ROUND(MIN(price_eur), 0) AS min_price,
       ROUND(MAX(price_eur), 0) AS max_price,
       COUNT(*)                 AS total_sales
FROM transactions
WHERE year IS NOT NULL
GROUP BY year
ORDER BY year
"""
pd.read_sql(q2, conn).to_csv(f"{OUT_DIR}/trend_by_year.csv", index=False)
print("Query 2 done: yearly trend")

# ── Query 3: Year-over-year % change ─────────────────────────────────
q3 = """
SELECT year,
       ROUND(AVG(price_eur), 0) AS avg_price,
       COUNT(*)                 AS total_sales,
       ROUND(
           (AVG(price_eur) - LAG(AVG(price_eur)) OVER (ORDER BY year))
           / LAG(AVG(price_eur)) OVER (ORDER BY year) * 100, 1
       ) AS pct_change
FROM transactions
WHERE year IS NOT NULL
GROUP BY year
ORDER BY year
"""
pd.read_sql(q3, conn).to_csv(f"{OUT_DIR}/yoy_change.csv", index=False)
print("Query 3 done: year-over-year change")

# ── Query 4: New vs second-hand by year ──────────────────────────────
q4 = """
SELECT year,
       is_new,
       ROUND(AVG(price_eur), 0) AS avg_price,
       COUNT(*)                 AS total_sales
FROM transactions
WHERE year IS NOT NULL
GROUP BY year, is_new
ORDER BY year, is_new
"""
pd.read_sql(q4, conn).to_csv(f"{OUT_DIR}/new_vs_secondhand.csv", index=False)
print("Query 4 done: new vs second-hand")

# ── Query 5: Monthly trend ────────────────────────────────────────────
q5 = """
SELECT year, month,
       ROUND(AVG(price_eur), 0) AS avg_price,
       COUNT(*)                 AS total_sales
FROM transactions
WHERE year IS NOT NULL AND month IS NOT NULL
GROUP BY year, month
ORDER BY year, month
"""
pd.read_sql(q5, conn).to_csv(f"{OUT_DIR}/monthly_trend.csv", index=False)
print("Query 5 done: monthly trend")

# ── Query 6: Dublin vs rest of Ireland ───────────────────────────────
q6 = """
SELECT year,
       is_dublin,
       ROUND(AVG(price_eur), 0) AS avg_price,
       COUNT(*)                 AS total_sales
FROM transactions
WHERE year IS NOT NULL
GROUP BY year, is_dublin
ORDER BY year, is_dublin
"""
pd.read_sql(q6, conn).to_csv(f"{OUT_DIR}/dublin_vs_rest.csv", index=False)
print("Query 6 done: Dublin vs rest")

conn.close()
print("\nAll queries complete. CSVs saved to data/processed/")
=======

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
>>>>>>> 9615b6eb1df91d666e09a27a0160fbf6acbc7196
