SELECT *
FROM (
    SELECT 
        d.doctor_id,
        d.first_name || ' ' || d.last_name AS doctor_name,
        SUM(b.amount) AS total_revenue,
        RANK() OVER (ORDER BY SUM(b.amount) DESC) AS revenue_rank
    FROM doctors d
    JOIN visits v ON d.doctor_id = v.doctor_id
    JOIN billing_claims b ON v.visit_id = b.visit_id
    WHERE b.status = 'Paid'
    GROUP BY d.doctor_id, doctor_name
) t
WHERE revenue_rank <= 10;