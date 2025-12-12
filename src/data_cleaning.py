import pandas as pd


def validate_and_clean(df):
    """
    Take a raw stock DataFrame and return a standardized version.
    Steps:
    - Ensure correct column names
    - Ensure no missing values in essential columns
    - Ensure dates are sorted and unique
    - Rename columns to consistent snake_case format
    """
    
    # 1. Check required columns
    required_cols = {
        "Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"
    }
    
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    # 2. Sort by date
    df = df.sort_values("Date").reset_index(drop=True)
    
    # 3. Ensure date uniqueness
    if df["Date"].duplicated().any():
        raise ValueError("Duplicate dates found in the dataset.")
    
    # 4. Check for missing values 
    essential_cols = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    
    for col in essential_cols:
        if df[col].isnull().any():
            raise ValueError(f"Column '{col}' contains missing values.")
    
    # 5. Rename columns for consistency 
    df = df.rename(columns={
        "Date": "date",
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Adj Close": "adj_close",
        "Volume": "volume"
    })
    
    # 6. Ensure correct dtypes
    df["date"] = pd.to_datetime(df["date"])
    
    numeric_cols = ["open", "high", "low", "close", "adj_close", "volume"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="raise")
    
    return df