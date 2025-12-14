from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import Huber


def build_lstm_model(input_shape, loss):
    """
    Build and compile an LSTM model for return prediction.

    Parameters:
    - input_shape: (timesteps, features)

    Returns:
    - compiled Keras model
    """

    model = Sequential()

    # LSTM layer
    model.add(
        LSTM(
            units=50,
            input_shape=input_shape
        )
    )

    # Output layer (predicts next-day return)
    model.add(Dense(1))

    # Compile the model

    if loss == "Huber":
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss=Huber(delta=0.01)
        )

    else :
        model.compile(
            optimizer=Adam(learning_rate=0.001),
            loss="mse"
        )

    return model
