import pandas as pd
import numpy as np

def add_returns(df, price_col="adj_close", method="log"):
    """
    Adds a returns column to the DataFrame.
    
    Parameters:
    - df: cleaned DataFrame with columns including 'adj_close'
    - price_col: column to compute returns on
    - method: "log" for log returns, "simple" for simple returns
    
    Returns:
    - df: DataFrame with a new column 'returns'
    """
    df = df.copy()
    
    if method == "log":
        df["returns"] = np.log(df[price_col] / df[price_col].shift(1))
    elif method == "simple":
        df["returns"] = df[price_col].pct_change()
    else:
        raise ValueError("method must be 'log' or 'simple'")
    
    df = df.dropna().reset_index(drop=True)
    return df