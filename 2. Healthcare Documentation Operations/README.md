
# Healthcare Documentation Operations Analytics

# Project Overview

This project simulates the operational environment of a healthcare facility involving patients, doctors, medical scribes, clinical notes, and billing claims. The main goal is to evaluate clinical operations, detect revenue leakage, assess scribe productivity, optimize database queries, and track patient journeys.

#  4-Layer Data Operations Strategy

## Layer 1: Data Ingestion & Structuring

I designed a structured healthcare database by ingesting raw CSV data into PostgreSQL and enforcing schema consistency.

### What I did:
- Created relational database tables for healthcare operations
- Converted raw data types (TEXT → TIMESTAMP/DATE where required)
- Established primary and foreign key relationships across entities


## Layer 2: Data Quality & Validation

I implemented SQL-based validation checks to identify critical data quality issues affecting healthcare operations and billing accuracy.

### Key Checks:
- Missing billing claims for recorded visits
- Invalid diagnosis and procedure codes
- Duplicate visit records
- Timestamp inconsistencies in clinical and billing data


## Layer 3: Business Metrics & Analytics

I developed key healthcare KPIs to monitor operational performance and financial health.

### Metrics Built:
- Claim rejection rate
- Revenue per doctor
- Patient retention rate
- Scribe productivity metrics
- Revenue leakage estimation

---

## Layer 4: Insights & Decision Support

I translated raw healthcare data into actionable business insights for operational improvement.

### Key Insights:
- Identified revenue leakage due to missing billing claims
- Detected high claim rejection rates in specific specialties
- Found productivity variations among medical scribes
- Analyzed patient visit behavior and retention patterns

# Final Strategy

This project was designed as an end-to-end healthcare data operations system.

First, raw data was structured into a relational PostgreSQL database with proper schema design and data type corrections.  
Next, a data validation layer was implemented to identify critical issues such as missing billing claims, duplicate visits, and invalid diagnosis mappings, which directly impact revenue and operational accuracy.  
On top of this, advanced SQL analytics were developed to generate key performance indicators including claim rejection rate, revenue trends, doctor performance, and patient retention.  
Finally, these insights were used to highlight operational inefficiencies, improve data quality, and support better decision-making in a healthcare environment.


#  Key Components

##  Synthetic Data Generation (`dataGenerate.py`)
Uses Python, Pandas, and Faker to generate realistic healthcare datasets including:
- 5,000+ patients
- 50 doctors
- 20,000 patient visits
- Clinical notes, diagnoses, procedures, and billing claims


##  Database Ingestion (`data_push.py`)
Automates ETL process using:
- PostgreSQL
- SQLAlchemy
- Pandas

This script loads generated CSV files into structured database tables.


##  Database Schema & Metadata (`meta_data.py`)
Utility script to extract and validate database structure:
- Table schemas
- Column names
- Data types
- Relationship validation


##  Advanced SQL Analytics (`queries/`)
A collection of SQL scripts designed for business intelligence and operational insights.


#  Project Structure

2. Healthcare Documentation Operations/
   ├── data/                               # Generated CSV datasets
   ├── queries/                            # SQL analytics scripts
   │   ├── claim_rejection_root_cause_analysis.sql
   │   ├── convert_data_type.sql
   │   ├── data_quality_score.sql
   │   ├── doctor_performance_ranking.sql
   │   ├── fraud_or_anomaly_detection.sql
   │   ├── index_optimization.sql
   │   ├── monthly_growth_trend_and_growth_rate.sql
   │   ├── patient_journey.sql
   │   ├── patient_retention.sql
   │   ├── revenue_leakage_analysis.sql
   │   └── scribe_productivity_vs_quality.sql
   ├── dataGenerate.py                     # Synthetic data generator
   ├── data_push.py                        # ETL to PostgreSQL
   ├── meta_data.py                        # Database schema inspector
   ├── .gitignore
   └── README.md



#  Setup and Installation

## 1. Prerequisites
- Python 3.8+
- PostgreSQL
- Required Python packages:
  - pandas
  - numpy
  - Faker
  - sqlalchemy
  - psycopg2-binary



## 2. Environment Setup

```bash
python -m venv env
source env/bin/activate   # Windows: .\env\Scripts\activate

pip install pandas numpy Faker sqlalchemy psycopg2-binary
````


## 3. Usage Guide

### Step 1: Generate Synthetic Data

```bash
python dataGenerate.py
```

### Step 2: Load Data into PostgreSQL

Ensure PostgreSQL is running and a database (e.g., `healthcare`) is created.

```bash
python data_push.py
```

---

### Step 3: Validate Database Schema

```bash
python meta_data.py
```

---

### Step 4: Run SQL Analytics

Execute SQL files inside the `queries/` folder using:

* pgAdmin
* DBeaver
* DataGrip

---

# 📊 Analytical Highlights

## 💰 Revenue Leakage Analysis

Identifies unbilled visits and calculates potential financial loss.

## 👨‍⚕️ Doctor Performance Analysis

Ranks doctors based on revenue generation and patient load.

## 📉 Data Quality Assessment

Detects:

* Missing values
* Invalid codes
* Data inconsistencies

## 🧑 Patient Retention Analysis

Tracks repeat visits and long-term patient engagement behavior.

---

# 🛠️ Technology Stack

* Python → Data generation & ETL
* Pandas → Data manipulation
* Faker → Synthetic data generation
* SQLAlchemy → Database connection layer
* PostgreSQL → Relational database
* SQL → Advanced analytics

---

# 🏁 Conclusion

This project demonstrates a complete **Healthcare Data Operations System**, covering:

* Data Engineering (ETL pipeline)
* Database Design (PostgreSQL schema)
* Data Quality Validation
* Advanced SQL Analytics
* Business Intelligence Insights

It simulates real-world healthcare operational challenges similar to production environments in healthcare analytics companies such as Augmedix.

