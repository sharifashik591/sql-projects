CREATE INDEX idx_visits_patient ON visits(patient_id);
CREATE INDEX idx_visits_doctor ON visits(doctor_id);
CREATE INDEX idx_claims_visit ON billing_claims(visit_id);
CREATE INDEX idx_claims_status ON billing_claims(status);