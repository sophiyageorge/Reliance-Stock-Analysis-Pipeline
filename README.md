# 📈 Reliance Stock Analysis - Cloud Data Pipeline Project

Welcome to my Reliance stock analysis project!  
This project demonstrates an end-to-end **automated data pipeline**, integrating data fetching, transformation, cloud storage, automation, and visualization.

---

## 🚀 Project Overview

- **Objective:** Fetch, clean, store, and visualize Reliance stock market data.
- **Automation:** Built using **Apache Airflow** running on an Azure Virtual Machine (VM).
- **Cloud Storage:** Data stored in **Azure MySQL Database**.
- **Visualization:** Interactive dashboard created using **Power BI**.

---

## 🔧 Tech Stack

| Component        | Technology                            |
|------------------|---------------------------------------|
| Data Source      | [yfinance](https://pypi.org/project/yfinance/) Python Library |
| Data Processing  | Python (Pandas, NumPy)                |
| Orchestration    | Apache Airflow (Azure VM - B2s)       |
| Cloud Database   | Azure MySQL Server                   |
| Visualization    | Microsoft Power BI                   |
| Hosting          | Azure Virtual Machine (Ubuntu)       |

---

## 📚 Project Structure

```bash
reliance-stock-analysis/
├── dags/
│   └── reliance_stock_etl.py        # Airflow DAG for ETL
├── scripts/
│   ├── fetch_data.py                 # Fetch data from yfinance
│   ├── clean_transform_data.py       # Clean and transform data
│   └── load_to_mysql.py              # Load data into Azure MySQL
├── powerbi/
│   └── reliance_stock_report.pbix    # Power BI report file
├── README.md                         # Project Documentation
└── requirements.txt                  # Python Dependencies
