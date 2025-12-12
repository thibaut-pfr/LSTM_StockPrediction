import os
import glob
import pandas as pd


def list_ticker_files(folder_path):
    """
    Return a sorted list of CSV file paths inside the dataset folder.
    This is used to know what tickers are available.
    """
    pattern = os.path.join(folder_path, "*.csv")
    return sorted(glob.glob(pattern))


def load_ticker_csv(file_path):
    """
    Load a single ticker CSV file and return a pandas DataFrame.
    Makes sure the Date column is parsed as a datetime object.
    """
    df = pd.read_csv(file_path, parse_dates=["Date"])
    
    # Check required columns exist
    required_cols = {"Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"}
    if not required_cols.issubset(df.columns):
        missing = required_cols - set(df.columns)
        raise ValueError(f"CSV file {file_path} is missing required columns: {missing}")

    # Sort by date
    df = df.sort_values("Date").reset_index(drop=True)
    
    return df


def load_ticker_by_symbol(folder_path, symbol):
    """
    Given a ticker symbol like 'AAPL', automatically finds and loads the CSV.
    """
    file_path = os.path.join(folder_path, f"{symbol}.csv")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No CSV found for ticker symbol: {symbol}")

    return load_ticker_csv(file_path)
