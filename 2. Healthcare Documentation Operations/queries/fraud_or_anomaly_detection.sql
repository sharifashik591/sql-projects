SELECT 
    patient_id,
    DATE(visit_datetime) AS visit_date,
    COUNT(*) AS visits
FROM visits
GROUP BY patient_id, visit_date
HAVING COUNT(*) > 3
ORDER BY visits DESC;