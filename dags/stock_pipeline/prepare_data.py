import pandas as pd

def prepare_data():
    # Step 1: Load the CSV
    df = pd.read_csv("/home/azureuser/stock_pipeline/raw_data.csv")

    # Step 2: Quick Overview
    print("Shape of data:", df.shape)
    print("Column names:", df.columns.tolist())
    print("data types",df.dtypes)
    print(df.head())

    # Step 3: Handle Missing Values
    # Drop rows with missing values or fill them
    df = df.dropna()

    # Step 4: Convert Date Column (if applicable)
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])

    # Step 5: Sort by Date (if applicable)
    if 'Date' in df_cleaned.columns:
        df = df.sort_values(by='Date')


    # df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]

    # Step 6: Create New Columns (Example: Daily Returns)
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    if 'Close' in df.columns:
        df['Daily Return'] = df['Close'].pct_change()

    # Step 7: Drop duplicates if any
    df = df.drop_duplicates()

    # Step 8: Drop missing values
    df = df.dropna()
    


    if df.isnull().values.any():
        print("⚠️ DataFrame contains NaN values.")
        print(df.isnull().sum())  # Optional: Shows count of NaNs per column
    else:
        print("✅ No NaN values in the DataFrame.")
    df.to_csv("/home/azureuser/stock_pipeline/cleaned_data.csv", index=False)
    return df
