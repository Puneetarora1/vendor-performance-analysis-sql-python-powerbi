# 📊 Vendor Performance Analysis using Python, SQL and Power BI
Analyzed vendor sales, purchase, and inventory data using SQL, Python, and Power BI to identify high-margin opportunities, reduce excess stock, and optimize purchasing decisions.

## 📌 Project Overview
- This project is an industry-style, end-to-end analytics workflow for a liquor retail and distribution business. 
- It covers the full pipeline- ingesting multi-million-row CSVs into a SQL database, building an analytical summary table with SQL, cleaning data in Python, EDA, statistical testing and an interactive Power BI dashboard.

---

## ❓ Problem Statement
The distributor serves to 100+ vendors, so distributor needs to analyze data to build effective inventory and sales management. This project aims to find

- Which vendors and brands drive the most revenue and profit?
- How dependent is procurement on a few vendors?
- Where is money tied up in slow-moving or unsold inventory?
- Does bulk buying actually lower unit cost?
- Which brands are high-margin but under-selling and need promotion?

---

## 📂 Dataset Description
- Dataset was stored in multiple csv files. (**~15.4M rows** in total, calendar year 2024),
- Created final analytical table: vendor_sales_summary with 10,692 rows and 18 columns, built with SQL CTEs and joins.

---

## 🛠️ Tech Stack
- **Data Ingestion** – 	Python, Pandas, SQLAlchemy
- **Database & SQL** – SQLite, CTEs, JOINs, GROUP BY aggregations
- **Analysis** – Pandas, NumPy, Statistics
- **Visualization** – Matplotlib, Seaborn, Power BI (DAX measures, interactive visuals)
  
---

## 🧹 Data Cleaning & Preparation
- **Data Ingestion:** Loaded multiple CSV files into SQLite using Python, processing the 12.8M-row sales dataset in 200K-row chunks.

- **SQL Data Extraction:** Used CTEs, joins, and aggregations to combine purchase, sales, and invoice data into a unified vendor data summary table.

- **Data Cleaning:** Handled missing values, corrected data types, and removed inconsistent records.

- **Feature Engineering:** Created key metrics, including Gross Profit, Profit Margin etc.

## 🔍 Exploratory Data Analysis
#### Corelation Analysis
- Weak between Purchase Price & Profit
- Strong between Purchase Qty & Sales Qty (0.999)
- Negative relationship between Profit Margin & Sales Price (-0.179)

## 🧪 Research Questions & Key Findings
- **Brands for Promotions and repricing:** 198 brands with low sales but high profit margins
- **Top Vendors**: top 10 of 119 vendors account for ~65.7% of purchase. Ther is a risk of over-reliance
- **Bulk Purchasing Impact:** 72% cost savings per unit in large orders
- **Inventory Turnover:** $2.71M worth of unsold inventory
- **Vendor Profitability:**
    - High-sales Vendors: Mean Margin = 31.17%
    - Low Vendors: Mean Margin = 41.55%
- **Hypothesis Testing:** Statistically significant difference in profit margins. 

## 📈 Visualizations
- **Transactions Over Time** – Tracks monthly transaction volume and transaction value.
- **Unsuccessful Transaction Reason Analysis** – Identifies major reasons behind unsuccessful transactions.
- **Service Transaction Value Analysis** – Compares transaction value across services such as Loans, Insurance, Money Transfer, and Recharge Bills.
- **Top 5 Users by Transaction Value** – Identifies users with the highest transaction values.
- **Age Segment Contribution** – Analyzes user distribution across different age segments.
- **Interactive Tooltips** – Provides additional details when users interact with dashboard visuals.
- **KPI Cards** – Provides a quick overview of important business metrics.
  
- ![Customer Segments](https://github.com/Puneetarora1/vendor-performance-analysis-sql-python-powerbi/blob/main/Reports%20and%20Dashbaord/Power%20BI%20Dashboard%20Snapshot.png)

---

## 🚀 Business Recommendations
- Diversify vendor base to reduce risk
- Optimize bulk order strategies
- Reprice slow-moving, high-margin brands
- Clear unsold inventory strategically
- Improve marketing for underperforming vendors

---

- ## 👤 Author & Contact
- Puneet Kumar
- Data Analyst
- puneetarora020@gmail.com
- [LinkedIn](https://www.linkedin.com/in/puneet-kumar1/)

---
