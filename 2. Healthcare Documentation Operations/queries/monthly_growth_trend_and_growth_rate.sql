WITH monthly_revenue AS (
    SELECT 
        DATE_TRUNC('month', claim_date) AS month,
        SUM(amount) AS revenue
    FROM billing_claims
    WHERE status = 'Paid'
    GROUP BY month
)
SELECT 
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month,
    ROUND(
        ((revenue - LAG(revenue) OVER (ORDER BY month)) * 100.0 
        / LAG(revenue) OVER (ORDER BY month))::numeric, 2  -- Cast to numeric here
    ) AS growth_rate
FROM monthly_revenue;
