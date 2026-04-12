SELECT
    order_date,
    total_sales,
    -- Running Total: Adds current month sales to all previous months
    SUM(total_sales) OVER (ORDER BY order_date) AS running_total_sales,
    -- Moving Average: Tracks the average price trend over time
    AVG(avg_price) OVER (ORDER BY order_date) AS moving_average_price
FROM
(
    SELECT 
        DATE_TRUNC('year', order_date) AS order_date, 
        SUM(sales_amount) AS total_sales, 
        AVG(price) AS avg_price
    FROM gold.fact_sales
    WHERE order_date IS NOT NULL
    GROUP BY DATE_TRUNC('year', order_date)
) t;