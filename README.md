Database used :
https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset

# 📊 E-commerce Sales Analysis (Pandas Project)

## 📌 Project Overview

This project analyzes an e-commerce retail dataset to extract meaningful business insights related to sales performance, customer behavior, and revenue trends.

The goal is to simulate how a data analyst would explore transactional data to support business decision-making.

---

## 🧰 Tools & Technologies

* Python
* Pandas

---

## 🔧 Data Processing Steps

* Loaded dataset using Pandas
* Created a new feature: **Revenue = Quantity × UnitPrice**
* Removed non-product entries (e.g., POSTAGE-related records) for product-level analysis
* Handled missing values (CustomerID used only where required)
* Converted date column to datetime format
* Extracted monthly data for time-based analysis

---

## 📊 Analysis Performed

### 1. Revenue Overview

* Calculated total revenue generated
* Computed total number of orders

### 2. Country Analysis

* Identified top countries contributing to revenue
* Observed geographic distribution of sales

### 3. Product Analysis

* Identified top revenue-generating products
* Evaluated whether revenue is concentrated or distributed across products

### 4. Time Analysis

* Analyzed monthly revenue trends
* Identified seasonal patterns in sales

### 5. Customer Analysis

* Identified top customers by revenue contribution

## 🔍 Key Insights

* The **United Kingdom dominates revenue**, contributing the majority of total sales, indicating strong geographic dependence.
* Revenue is **distributed across multiple products**, with no single product overwhelmingly dominating sales.
* Sales show an **increase in the later months of the year**, suggesting possible seasonal demand (e.g., holiday period).
* A **small group of customers contributes significantly to revenue**, highlighting the importance of high-value customers.

## 🎯 Conclusion

This project demonstrates how raw transactional data can be transformed into actionable business insights using Pandas. It highlights key analytical steps such as data cleaning, feature engineering, aggregation, and interpretation.

