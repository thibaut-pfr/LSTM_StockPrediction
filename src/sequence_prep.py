import numpy as np

def create_lstm_sequences(df, feature_col, target_col, lookback):
    """
    Convert a time series DataFrame into LSTM-compatible sequences.

    Parameters:
    - df: DataFrame containing features and target
    - feature_col: column name used as LSTM input (e.g. 'returns')
    - target_col: column name to predict (e.g. 'returns')
    - lookback: number of past timesteps to include

    Returns:
    - X: numpy array of shape (samples, lookback, 1)
    - y: numpy array of shape (samples,)
    """

    X = []
    y = []

    values = df[feature_col].values
    targets = df[target_col].values

    for i in range(lookback, len(df)):
        X.append(values[i - lookback:i])
        y.append(targets[i])

    X = np.array(X)
    y = np.array(y)

    # LSTM expects 3D input: (samples, timesteps, features)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    return X, y
