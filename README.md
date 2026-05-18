Irish Housing Market — SQL Analytics Dashboard

## What this project does
Analyses 500,000+ residential property transactions from Ireland's
Property Price Register using SQL and Python. Results are visualised
in an interactive Power BI dashboard.

## Business questions answered
- Which county has the highest average house price?
- How have prices changed year over year since 2010?
- What is the total volume of sales per year?

## Tools used
Python · SQLite · pandas · SQL (CTEs, window functions) · Power BI

## Key findings
- Dublin consistently has the highest average price (€XXX,XXX in 2023)
- Prices peaked in 20XX and dipped in 20XX following [brief context]
- Cork and Galway show the next highest average prices

## How to run
1. Clone this repo
2. Download PPR data from data.gov.ie and save to data/raw/
3. Run: python notebooks/load_data.py
4. Run: python notebooks/run_queries.py
5. Open dashboard/housing.pbix in Power BI Desktop

## Skills demonstrated
Advanced SQL · Data cleaning with pandas · Power BI · SQLite
