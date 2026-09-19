-- 1. Revenue and profit by region
SELECT region,
       SUM(revenue) AS revenue,
       SUM(profit) AS profit,
       ROUND(SUM(profit)/NULLIF(SUM(revenue),0)*100,2) AS profit_margin_pct
FROM retail_sales
GROUP BY region
ORDER BY profit DESC;

-- 2. Category performance
SELECT category,
       SUM(revenue) AS revenue,
       SUM(profit) AS profit,
       SUM(quantity) AS units
FROM retail_sales
GROUP BY category
ORDER BY profit DESC;

-- 3. Product performance
SELECT product_name,
       SUM(revenue) AS revenue,
       SUM(profit) AS profit,
       SUM(quantity) AS units
FROM retail_sales
GROUP BY product_name
ORDER BY profit DESC;

-- 4. Discount vs profitability
SELECT discount,
       AVG(revenue) AS avg_revenue,
       AVG(profit) AS avg_profit,
       AVG(profit/revenue)*100 AS avg_margin_pct
FROM retail_sales
GROUP BY discount
ORDER BY discount;

-- 5. Monthly trend
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(revenue) AS revenue,
       SUM(profit) AS profit
FROM retail_sales
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;
