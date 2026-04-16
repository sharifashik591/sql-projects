-- Fix visit_datetime
ALTER TABLE visits
ALTER COLUMN visit_datetime TYPE TIMESTAMP
USING visit_datetime::timestamp;

-- Fix claim_date
ALTER TABLE billing_claims
ALTER COLUMN claim_date TYPE DATE
USING claim_date::date;

-- Fix created_at
ALTER TABLE clinical_notes
ALTER COLUMN created_at TYPE TIMESTAMP
USING created_at::timestamp;