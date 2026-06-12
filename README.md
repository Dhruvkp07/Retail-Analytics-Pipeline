# Retail-Analytics-Pipeline

## Overview

This project demonstrates an end-to-end Retail Analytics Pipeline built using Python, Pandas, SQLite, SQL, and Power BI.

The pipeline extracts product data from an API, transforms and cleans the data, stores it in a SQLite database, performs SQL-based business analysis, and visualizes key insights through an interactive Power BI dashboard.

---

## Dashboard Preview

![Dashboard](dashboard.png)

---

## Project Architecture

```text
FakeStore API
      ↓
Python (Requests)
      ↓
Pandas Data Cleaning
      ↓
CSV Dataset
      ↓
SQLite Database
      ↓
SQL Analysis
      ↓
Power BI Dashboard
```

---

## Technologies Used

* Python
* Pandas
* Requests
* SQLite
* SQL
* Matplotlib
* Power BI

---

## Project Structure

```text
Retail-Analytics-Pipeline
│
├── README.md
├── main.py
├── database.py
├── Retail_Analytics_Dashboard.pbix
│
├── data
│   └── products_cleaned.csv
│
├── database
│   └── products.db
│
├── charts
│   ├── category_distribution.png
│   └── top_rated_products.png
│
└── dashboard.png
```

---

## Features

### Data Extraction

* Extracts product data from FakeStore API
* Retrieves product details, pricing, categories, and ratings

### Data Transformation

* Converts JSON data into a Pandas DataFrame
* Extracts nested rating information
* Creates separate rating metrics
* Removes unnecessary fields

### Data Storage

* Exports cleaned data to CSV
* Stores processed data in SQLite database

### SQL Analysis

Performs business-oriented analysis using SQL queries:

* Product count by category
* Average price by category
* Total reviews by category
* Category performance comparison

### Dashboard Development

Interactive Power BI dashboard featuring:

* Total Products KPI
* Average Price KPI
* Average Rating KPI
* Total Reviews KPI
* Products by Category
* Average Price by Category
* Total Reviews by Category
* Category Slicer Filter

---

## Key Insights

### Product Distribution

| Category         | Products |
| ---------------- | -------: |
| Electronics      |        6 |
| Women's Clothing |        6 |
| Jewelery         |        4 |
| Men's Clothing   |        4 |

### Average Price by Category

| Category         | Average Price |
| ---------------- | ------------: |
| Electronics      |        332.50 |
| Jewelery         |        221.00 |
| Men's Clothing   |         51.06 |
| Women's Clothing |         26.29 |

### Total Reviews by Category

| Category         | Reviews |
| ---------------- | ------: |
| Electronics      |    1782 |
| Women's Clothing |    1675 |
| Men's Clothing   |    1309 |
| Jewelery         |     970 |

---

## Skills Demonstrated

* Data Extraction
* Data Cleaning
* ETL Pipeline Development
* Exploratory Data Analysis (EDA)
* SQL Querying
* Database Management
* Data Visualization
* Dashboard Development
* Business Analytics

---

## Future Improvements

* Integrate larger real-world retail datasets
* Automate data refresh using scheduling tools
* Add advanced SQL analytics
* Include customer segmentation analysis
* Deploy dashboard through Power BI Service

---

## Author

**Dhruv**

Aspiring Data Analyst | Python | SQL | Power BI | Data Analytics

