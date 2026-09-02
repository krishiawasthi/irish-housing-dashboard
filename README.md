# Irish Housing Market — SQL Analytics Dashboard

An end-to-end data analytics project analysing 287,590 residential 
property transactions from Ireland's Property Price Register (2010–2026), 
built using Python, SQLite, SQL, and Google Looker Studio.

---

## Live Dashboard

**[View Interactive Dashboard on Google Looker Studio](https://datastudio.google.com/reporting/e9627e9d-70a2-4cdf-9331-0f4c5c40ef32)**

![Irish Housing Market Dashboard](image)

---

## What this project does

Collects, cleans, and analyses 16 years of Irish residential property 
sales data to surface insights on price trends, regional disparities, 
new build vs second-hand dynamics, and the Dublin premium.

---

## Business questions answered

- Which county has the highest average house price?
- How have prices changed year over year since 2010?
- What is the Dublin premium over the rest of Ireland?
- How do new build prices compare to second-hand properties?
- Which years saw the biggest price increases and crashes?

---

## Key findings

- Dublin average price (€455K) is nearly double the national average
- Prices crashed 12% in 2011 and 8% in 2012 following the financial crisis
- Strong recovery from 2013, with prices rising consistently to 2026
- New builds command a significant premium over second-hand properties
- Longford is the most affordable county; Wicklow and Kildare follow Dublin

---

## Tools used

Python · SQLite · pandas · SQL (CTEs, window functions, aggregations) · 
Google Looker Studio · openpyxl

---

## Project structure

irish-housing-dashboard/
├── data/
│ ├── raw/ # Raw CSV from Property Price Register
│ └── processed/ # SQLite database and query output CSVs
├── notebooks/
│ ├── load_data.py # Cleans and loads data into SQLite
│ └── run_queries.py # Runs SQL queries and exports CSVs
├── sql/
│ └── queries.sql # All SQL queries
└── README.md

---

## How to run

1. Clone this repo
2. Download the Property Price Register dataset from 
   [Kaggle](https://www.kaggle.com/datasets/fionnhughes/property-price-register) 
   and save to `data/raw/property_price_register.csv`
3. Run: `python3 notebooks/load_data.py`
4. Run: `python3 notebooks/run_queries.py`
5. Open the Looker Studio dashboard link above

---

## Skills demonstrated

- Data cleaning and transformation with Python and pandas
- Database design and SQL querying (CTEs, window functions, 
  year-over-year analysis)
- Business intelligence and dashboard design in Google Looker Studio
- End-to-end analytics pipeline from raw data to interactive visualisation
- Working with large real-world government datasets (287,590 rows)
