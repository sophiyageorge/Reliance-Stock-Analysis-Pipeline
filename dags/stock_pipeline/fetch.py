import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker="RELIANCE.NS", start="2023-01-01", end="2023-12-31"):
    data = yf.download(ticker, start=start, end=end)
    data.reset_index(inplace=True)
    data.to_csv("/home/azureuser/airflow/dags/data/stock_data.csv", index=False)
    return data
