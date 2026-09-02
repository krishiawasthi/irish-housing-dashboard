-- Query 1: Average house price by county (sorted highest first)
-- GROUP BY groups all rows for each county together
-- AVG() calculates the average price within each group
-- ORDER BY sorts the result, DESC = highest first
SELECT county,
       ROUND(AVG(price), 2) AS avg_price,
       COUNT(*) AS total_sales
FROM transactions
GROUP BY county
ORDER BY avg_price DESC;

-- Query 2: Average price per year (to see the trend over time)
SELECT year,
       ROUND(AVG(price), 2) AS avg_price,
       COUNT(*) AS total_sales
FROM transactions
GROUP BY year
ORDER BY year;

-- Query 3: Year-over-year price change using a window function
-- LAG() looks at the previous row's value (previous year's avg price)
-- This lets us calculate how much prices changed each year
SELECT year,
       ROUND(AVG(price), 2) AS avg_price,
       ROUND(AVG(price) - LAG(AVG(price)) OVER (ORDER BY year), 2) AS yoy_change
FROM transactions
GROUP BY year
ORDER BY year;

-- Query 4: Top 10 most expensive counties this year
SELECT county,
       ROUND(AVG(price), 2) AS avg_price
FROM transactions
WHERE year = 2023
GROUP BY county
ORDER BY avg_price DESC
LIMIT 10;