import numpy as np
import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore


with open("ton_1704110400000_1729087900000.txt", "r") as file:
    dataRaw = [float(line.strip()) for line in file]



dataDiff = list()
for i in range(len(dataRaw)-1):
    dataDiff.append(dataRaw[i+1] - dataRaw[i])
downScale = 1 / abs(max(dataDiff, key=abs))
for i in range(len(dataDiff)):
    dataDiff[i] = dataDiff[i] * downScale


# Function to create sequences of data
def create_sequences(data, lookback=200):
    sequences = []
    targets = []
    for i in range(0, len(data) - lookback - 30, 5):
        sequences.append(data[i:i + lookback])
        targets.append(sum(data[i + lookback : i + lookback + 30]) * 1)
    # print(targets)
    # print(max(targets, key=abs))
    # print(max(targets, key=abs) / downScale)
    return np.array(sequences), np.array(targets)

lookback = 200
sequences, targets = create_sequences(dataDiff, lookback=lookback)

# Train/Test Split
train_size = int(len(sequences) * 0.9)
X_train, X_test = sequences[:train_size], sequences[train_size:]
y_train, y_test = targets[:train_size], targets[train_size:]

# Reshape the input data to be 3D as required by LSTM
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))  # Adding the feature dimension
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))


# Normalize/Scale the data
# scaler = MinMaxScaler()
# X_train = scaler.fit_transform(X_train.reshape(-1, X_train.shape[-1])).reshape(X_train.shape)
# X_test = scaler.transform(X_test.reshape(-1, X_test.shape[-1])).reshape(X_test.shape)

# 2. Model Creation

# Create the model
model = models.Sequential([
    layers.Input(shape=(lookback, X_train.shape[-1])),  # Input layer
    # layers.LSTM(128, activation='relu', return_sequences=True),
    # layers.LSTM(256, activation='relu', return_sequences=True),
    layers.LSTM(128, activation='relu', return_sequences=True),
    layers.LSTM(64, activation='relu', return_sequences=True),  # LSTM layer with 64 units
    layers.LSTM(32, activation='relu'),  # Another LSTM layer with 32 units
    layers.Dense(32, activation='relu'),  # Fully connected layer
    layers.Dropout(0.2),  # Dropout layer to prevent overfitting
    layers.Dense(1)  # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='mean_absolute_error',
              metrics=['mean_absolute_error'])
            #   metrics=['mean_absolute_error', "precision", "recall"])

# 3. Model Training
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

# 4. Model Evaluation
evaluation = model.evaluate(X_test, y_test)
print(f"Test MAE: {evaluation[1]}")
# print(f"Test Precision: {evaluation[2]}")
# print(f"Test Recall: {evaluation[3]}")

# 5. Predicting on New Data
# Example of predicting on a new sequence
new_sequence = X_test[0].reshape(1, lookback, X_train.shape[-1])
probability = model.predict(new_sequence)
print(f"Highest price in  next 30 mins: {probability[0][0]}")
