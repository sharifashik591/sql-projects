import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# CONFIG
# -----------------------------
NUM_PATIENTS = 5000
NUM_DOCTORS = 50
NUM_SCRIBES = 20
NUM_VISITS = 20000

# -----------------------------
# HELPER LISTS
# -----------------------------
genders = ['M', 'F']
specialties = ['Cardiology', 'Neurology', 'Orthopedics', 'General', 'Dermatology']
training_levels = ['Junior', 'Mid', 'Senior']

diagnosis_codes = [
    ('I10', 'Hypertension'),
    ('E11', 'Type 2 Diabetes'),
    ('J20', 'Bronchitis'),
    ('M54', 'Back Pain'),
    ('F41', 'Anxiety Disorder')
]

procedure_codes = [
    ('99213', 'Consultation'),
    ('93000', 'ECG'),
    ('80050', 'Blood Test'),
    ('71020', 'X-Ray'),
    ('12001', 'Minor Surgery')
]

insurance_plans = ['Aetna', 'BlueCross', 'UnitedHealth', 'Cigna']

# -----------------------------
# PATIENT TABLE
# -----------------------------
patients = []
for i in range(1, NUM_PATIENTS + 1):
    patients.append([
        i,
        fake.first_name(),
        fake.last_name(),
        random.randint(1950, 2010),
        random.choice(genders)
    ])

patients_df = pd.DataFrame(patients, columns=[
    'patient_id', 'first_name', 'last_name', 'birth_year', 'gender'
])

# -----------------------------
# DOCTOR TABLE
# -----------------------------
doctors = []
for i in range(1, NUM_DOCTORS + 1):
    doctors.append([
        i,
        fake.first_name(),
        fake.last_name(),
        random.choice(specialties)
    ])

doctors_df = pd.DataFrame(doctors, columns=[
    'doctor_id', 'first_name', 'last_name', 'specialty'
])

# -----------------------------
# SCRIBE TABLE
# -----------------------------
scribes = []
for i in range(1, NUM_SCRIBES + 1):
    scribes.append([
        i,
        fake.first_name(),
        fake.last_name(),
        random.choice(training_levels)
    ])

scribes_df = pd.DataFrame(scribes, columns=[
    'scribe_id', 'first_name', 'last_name', 'training_level'
])

# -----------------------------
# VISIT TABLE
# -----------------------------
visits = []
start_date = datetime(2022, 1, 1)

for i in range(1, NUM_VISITS + 1):
    visit_time = start_date + timedelta(days=random.randint(0, 1000))
    
    visits.append([
        i,
        random.randint(1, NUM_PATIENTS),
        random.randint(1, NUM_DOCTORS),
        random.randint(1, NUM_SCRIBES),
        visit_time,
        fake.city()
    ])

visits_df = pd.DataFrame(visits, columns=[
    'visit_id', 'patient_id', 'doctor_id', 'scribe_id', 'visit_datetime', 'location'
])

# -----------------------------
# CLINICAL NOTE TABLE
# -----------------------------
notes = []
for i in range(1, NUM_VISITS + 1):
    notes.append([
        i,
        i,
        fake.paragraph(nb_sentences=5),
        datetime.now()
    ])

notes_df = pd.DataFrame(notes, columns=[
    'note_id', 'visit_id', 'content', 'created_at'
])

# -----------------------------
# VISIT DIAGNOSIS
# -----------------------------
visit_diag = []
for visit_id in range(1, NUM_VISITS + 1):
    for _ in range(random.randint(1, 3)):
        code = random.choice(diagnosis_codes)
        visit_diag.append([visit_id, code[0]])

visit_diag_df = pd.DataFrame(visit_diag, columns=[
    'visit_id', 'diag_code'
])

diag_df = pd.DataFrame(diagnosis_codes, columns=[
    'diag_code', 'description'
])

# -----------------------------
# VISIT PROCEDURE
# -----------------------------
visit_proc = []
for visit_id in range(1, NUM_VISITS + 1):
    for _ in range(random.randint(1, 2)):
        code = random.choice(procedure_codes)
        visit_proc.append([visit_id, code[0]])

visit_proc_df = pd.DataFrame(visit_proc, columns=[
    'visit_id', 'proc_code'
])

proc_df = pd.DataFrame(procedure_codes, columns=[
    'proc_code', 'description'
])

# -----------------------------
# BILLING CLAIMS
# -----------------------------
claims = []
for i in range(1, NUM_VISITS + 1):
    claims.append([
        i,
        i,
        random.choice(insurance_plans),
        fake.date_between(start_date='-2y', end_date='today'),
        round(random.uniform(50, 500), 2),
        random.choice(['Paid', 'Pending', 'Rejected'])
    ])

claims_df = pd.DataFrame(claims, columns=[
    'claim_id', 'visit_id', 'insurance_plan', 'claim_date', 'amount', 'status'
])

# -----------------------------
# SAVE FILES
# -----------------------------
patients_df.to_csv('patients.csv', index=False)
doctors_df.to_csv('doctors.csv', index=False)
scribes_df.to_csv('scribes.csv', index=False)
visits_df.to_csv('visits.csv', index=False)
notes_df.to_csv('clinical_notes.csv', index=False)
visit_diag_df.to_csv('visit_diagnosis.csv', index=False)
diag_df.to_csv('diagnosis_codes.csv', index=False)
visit_proc_df.to_csv('visit_procedure.csv', index=False)
proc_df.to_csv('procedure_codes.csv', index=False)
claims_df.to_csv('billing_claims.csv', index=False)

print("✅ All datasets generated successfully!")