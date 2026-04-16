SELECT 
    COUNT(v.visit_id) AS total_visits,
    COUNT(b.claim_id) AS billed_visits,
    COUNT(v.visit_id) - COUNT(b.claim_id) AS missing_claims,
    ROUND(
        (COUNT(v.visit_id) - COUNT(b.claim_id)) * 100.0 / COUNT(v.visit_id), 2
    ) AS leakage_percentage
FROM visits v
LEFT JOIN billing_claims b ON v.visit_id = b.visit_id;