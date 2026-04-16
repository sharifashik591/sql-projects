SELECT 
    'Missing Claims' AS issue,
    COUNT(*) AS count
FROM visits v
LEFT JOIN billing_claims b ON v.visit_id = b.visit_id
WHERE b.visit_id IS NULL

UNION ALL

SELECT 
    'Invalid Diagnosis Codes',
    COUNT(*)
FROM visit_diagnosis vd
LEFT JOIN diagnosis_codes dc ON vd.diag_code = dc.diag_code
WHERE dc.diag_code IS NULL

UNION ALL

SELECT 
    'Duplicate Visits',
    COUNT(*)
FROM (
    SELECT visit_id
    FROM visits
    GROUP BY visit_id
    HAVING COUNT(*) > 1
) t;