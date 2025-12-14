def time_series_split(X, y, train_ratio=0.7, val_ratio=0.15):
    """
    Split time series data into train / validation / test sets
    without shuffling.

    Parameters:
    - X: input sequences (samples, timesteps, features)
    - y: targets
    - train_ratio: fraction used for training
    - val_ratio: fraction used for validation

    Returns:
    - X_train, y_train
    - X_val, y_val
    - X_test, y_test
    """

    n_samples = len(X)

    train_end = int(n_samples * train_ratio)
    val_end = int(n_samples * (train_ratio + val_ratio))

    X_train = X[:train_end]
    y_train = y[:train_end]

    X_val = X[train_end:val_end]
    y_val = y[train_end:val_end]

    X_test = X[val_end:]
    y_test = y[val_end:]

    return X_train, y_train, X_val, y_val, X_test, y_test
