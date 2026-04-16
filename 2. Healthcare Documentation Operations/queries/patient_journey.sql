SELECT 
    p.patient_id,
    p.first_name || ' ' || p.last_name AS patient_name,
    v.visit_id,
    v.visit_datetime,
    d.first_name || ' ' || d.last_name AS doctor_name,
    s.first_name || ' ' || s.last_name AS scribe_name,
    b.amount,
    b.status
FROM patients p
JOIN visits v ON p.patient_id = v.patient_id
JOIN doctors d ON v.doctor_id = d.doctor_id
JOIN scribes s ON v.scribe_id = s.scribe_id
LEFT JOIN billing_claims b ON v.visit_id = b.visit_id
ORDER BY v.visit_datetime DESC;