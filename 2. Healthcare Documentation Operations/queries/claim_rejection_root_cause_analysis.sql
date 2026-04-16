SELECT 
    d.specialty,
    COUNT(*) AS total_claims,
    SUM(CASE WHEN b.status = 'Rejected' THEN 1 ELSE 0 END) AS rejected,
    ROUND(
        SUM(CASE WHEN b.status = 'Rejected' THEN 1 ELSE 0 END) * 100.0 
        / COUNT(*), 2
    ) AS rejection_rate
FROM billing_claims b
JOIN visits v ON b.visit_id = v.visit_id
JOIN doctors d ON v.doctor_id = d.doctor_id
GROUP BY d.specialty
ORDER BY rejection_rate DESC;