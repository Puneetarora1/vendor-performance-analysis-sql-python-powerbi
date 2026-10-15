# 📊 Vendor Performance Analysis using Python, SQL and Power BI
Analyzed vendor sales, purchase, and inventory data using SQL, Python, and Power BI to identify high-margin opportunities, reduce excess stock, and optimize purchasing decisions.

## 📌 Project Overview
This project is an industry-style, end-to-end analytics workflow for a liquor retail and distribution business. 
It covers the full pipeline- ingesting multi-million-row CSVs into a SQL database, building an analytical summary table with SQL, cleaning data in Python, EDA, statistical testing and an interactive Power BI dashboard.

---

## ❓ Problem Statement
The distributor serves to 100+ vendors, so distributor needs to analyze data to build effective inventory and sales management. This project aims to find

Which vendors and brands drive the most revenue and profit?
How dependent is procurement on a few vendors?
Where is money tied up in slow-moving or unsold inventory?
Does bulk buying actually lower unit cost?
Which brands are high-margin but under-selling and need promotion?

---

## 📂 Dataset Description
- Dataset was stored in multiple csv files. (~15.4M rows in total, calendar year 2024),
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

**Data Cleaning:** Handled missing values, corrected data types, and removed inconsistent records.

**Feature Engineering:** Created key metrics, including Gross Profit, Profit Margin etc.

### 🔍 Exploratory Data Analysis
#### Corelation Analysis
- Weak between Purchase Price & Profit
- Strong between Purchase Qty & Sales Qty (0.999)
- Negative relationship between Profit Margin & Sales Price (-0.179)

### 🧪 Research Questions & Key Findings
- **Brands for Promotions and repricing:** 198 brands with low sales but high profit margins
- **Top Vendors**: top 10 of 119 vendors account for ~65.7% of purchase. Ther is a risk of over-reliance
- **Bulk Purchasing Impact:** 72% cost savings per unit in large orders
- **Inventory Turnover:** $2.71M worth of unsold inventory
- **Vendor Profitability:**
o High Vendors: Mean Margin = 31.17%
o Low Vendors: Mean Margin = 41.55%
6. Hypothesis Testing: Statistically significant difference in profit margins > distinct vendor strategies

### 📈 Visualizations
- **Transactions Over Time** – Tracks monthly transaction volume and transaction value.
- **Unsuccessful Transaction Reason Analysis** – Identifies major reasons behind unsuccessful transactions.
- **Service Transaction Value Analysis** – Compares transaction value across services such as Loans, Insurance, Money Transfer, and Recharge Bills.
- **Top 5 Users by Transaction Value** – Identifies users with the highest transaction values.
- **Age Segment Contribution** – Analyzes user distribution across different age segments.
- **Interactive Tooltips** – Provides additional details when users interact with dashboard visuals.
- **KPI Cards** – Provides a quick overview of important business metrics.

---

## 💡 Key Insights
- The dashboard recorded **300K+ total transactions** with a total transaction value of approximately **₹3.47 Billion**.
- The overall successful transaction rate was **98.40%**, indicating strong transaction success performance.
- **Loans** recorded the highest transaction value among the analyzed services, contributing approximately **₹2.5 Billion**.
- Among unsuccessful transactions, **Server Errors, Wrong PIN, and Insufficient Amount** were the major contributing reasons.
- Users aged **26–58** represented approximately **three-fourths of total users**.

---

## 🚀 Business Recommendations
- 🔧 Reduce transaction failures by addressing major failure reasons.
- 🏦 Focus on high-value services such as **Loans**.
- 🎯 Develop targeted strategies for the core **26–58 age segment**.
- 📊 Monitor monthly KPIs and retain high-value users.

---

- ## 📷 Project Snapshot
- ![Customer Segments](https://github.com/Puneetarora1/PhonePe-Data-Analysis-Project/blob/main/Report%20Snapshot.png)

---
```
