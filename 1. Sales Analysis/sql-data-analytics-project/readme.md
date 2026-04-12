# 🟡 Gold Sales Intelligence – SQL Analytics Project ([Documentation](https://docs.google.com/document/d/1QaCR51aRXDn8WgntIT8czFkmgNo4SxC2IRVUEIO7GDM/edit?usp=sharing))

## 📌 Overview

The Gold Sales Intelligence Project is a complete SQL-based analytics solution designed to transform raw sales data into meaningful business insights.

This project demonstrates how structured data modeling and advanced SQL techniques can be used to analyze customer behavior, product performance, and revenue trends in a real-world scenario.

It is built as a portfolio-ready project showcasing practical, industry-level data analytics skills.

## 🏗️ Data Architecture

The project follows a Star Schema model, optimized for analytical queries.

### 🔹 Schema: `gold`

#### 📊 Fact Table
- **`fact_sales`**
  - Stores transactional sales data
  - Includes: sales amount, quantity, price
  - Connected to dimensions via surrogate keys

#### 👥 Dimension Tables
- **`dim_customers`**
  - Customer demographics and attributes
- **`dim_products`**
  - Product details, categories, and cost

## 📂 Project Structure
```text
📁 sql-query/
   ├── database_setup.sql
   ├── exploratory_analysis.sql
   ├── magnitude_analysis.sql
   ├── ranking_analysis.sql
   ├── time_analysis.sql
   ├── cumulative_analysis.sql
   ├── performance_analysis.sql
   ├── segmentation_analysis.sql
   ├── reports.sql
```

## 📖 Full Documentation

👉 **Detailed documentation:**
🔗 [Read the Documentation](https://docs.google.com/document/d/1QaCR51aRXDn8WgntIT8czFkmgNo4SxC2IRVUEIO7GDM/edit?usp=sharing)

Includes:
- Query explanations
- Business logic
- Step-by-step analysis

## ⚙️ Database Setup

- **Database:** PostgreSQL
- **Data Source:** CSV files
- **Loading Method:** `COPY` command

**Steps:**
1. Create database
2. Run schema & table scripts
3. Update CSV file paths
4. Load data using `COPY`
5. Execute analysis queries

## 🔍 Exploratory Analysis

Performed to understand data structure and validate quality.

**Key Metrics:**
- Total Sales
- Total Orders
- Average Price
- Total Customers

## 📊 Analytical Modules

### 📌 Magnitude Analysis
- Customers by country & gender
- Revenue by category

### 🏆 Ranking Analysis
- Top & worst products
- Top customers

### 📈 Change Over Time
- Sales trends
- Monthly & yearly performance

### 🔄 Cumulative Analysis
- Running total of sales

### 📉 Performance Analysis
- YoY & MoM comparisons

### 🎯 Segmentation
- VIP, Regular, New customers
- Product cost segments

### 🧩 Part-to-Whole
- Category contribution to total sales

## 📑 Reporting

### 👤 Customer Report
- Total orders, sales, quantity
- **KPIs:**
  - Recency
  - Avg order value
  - Monthly spend

### 📦 Product Report
- Performance classification
- Revenue insights
- Product KPIs

## 💡 Key Outcomes
- Strong SQL analytics skills
- Real-world data modeling
- Business-focused insights
- End-to-end analytics workflow

## 🛠️ Technologies Used
- PostgreSQL
- SQL
- CSV Data

## 🚀 Future Improvements
- Power BI / Tableau dashboards
- Automated ETL pipeline
- Predictive analytics
- Query optimization

## 👨‍💻 Author

**Sharif Ashik Ishtiak**
- 📞 **Phone:** 01944896737
- 📧 **Email:** sharifashik591@gmail.com
