SELECT 
    v.scribe_id,
    COUNT(v.visit_id) AS total_visits,
    ROUND(AVG(LENGTH(n.content)), 2) AS avg_note_length,
    ROUND(COUNT(v.visit_id) * 1.0 / COUNT(DISTINCT DATE(v.visit_datetime)), 2) AS visits_per_day
FROM visits v
JOIN clinical_notes n ON v.visit_id = n.visit_id
GROUP BY v.scribe_id
ORDER BY total_visits DESC;