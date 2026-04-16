WITH first_visit AS (
    SELECT 
        patient_id, 
        MIN(visit_datetime) AS first_date
    FROM visits
    GROUP BY patient_id
),
cohort AS (
    SELECT 
        v.patient_id,
        DATE_TRUNC('month', f.first_date) AS cohort_month,
        DATE_TRUNC('month', v.visit_datetime) AS visit_month
    FROM visits v
    JOIN first_visit f ON v.patient_id = f.patient_id
)
SELECT 
    cohort_month,
    visit_month,
    COUNT(DISTINCT patient_id) AS active_patients
FROM cohort
GROUP BY cohort_month, visit_month
ORDER BY cohort_month, visit_month;