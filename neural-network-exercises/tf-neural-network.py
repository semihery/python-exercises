import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from tensorflow.python.keras import layers, models

# 1. Data Preparation
# Assume we have a DataFrame `df` with columns: ['price_change', 'volume', 'rsi', 'macd', ...]

# Simulating some sample data for demonstration
np.random.seed(42)
data_size = 1000
df = pd.DataFrame({
    'price_change': np.random.randn(data_size),
    'volume': np.random.rand(data_size),
    'rsi': np.random.rand(data_size) * 100,
    'macd': np.random.randn(data_size),
    # Add more technical indicators as needed
})

# Function to create sequences of data
def create_sequences(data, lookback=100):
    sequences = []
    targets = []
    for i in range(len(data) - lookback):
        sequences.append(data[i:i + lookback])
        targets.append(1 if data[i + lookback][0] > 0 else 0)  # Binary target: 1 if price goes up, else 0
    return np.array(sequences), np.array(targets)

# Generate sequences and targets
lookback = 100
sequences, targets = create_sequences(df.values, lookback=lookback)

# Train/Test Split
train_size = int(len(sequences) * 0.7)
X_train, X_test = sequences[:train_size], sequences[train_size:]
y_train, y_test = targets[:train_size], targets[train_size:]

# Normalize/Scale the data
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train.reshape(-1, X_train.shape[-1])).reshape(X_train.shape)
X_test = scaler.transform(X_test.reshape(-1, X_test.shape[-1])).reshape(X_test.shape)

# 2. Model Creation

# Create the model
model = models.Sequential([
    layers.Input(shape=(lookback, X_train.shape[-1])),  # Input layer
    layers.LSTM(64, activation='relu', return_sequences=True),  # LSTM layer with 64 units
    layers.LSTM(32, activation='relu'),  # Another LSTM layer with 32 units
    layers.Dense(32, activation='relu'),  # Fully connected layer
    layers.Dropout(0.2),  # Dropout layer to prevent overfitting
    layers.Dense(1, activation='sigmoid')  # Output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy', tf.keras.metrics.AUC()])

# 3. Model Training
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# 4. Model Evaluation
evaluation = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {evaluation[1]}")
print(f"Test AUC: {evaluation[2]}")

# 5. Predicting on New Data
# Example of predicting on a new sequence
new_sequence = X_test[0].reshape(1, lookback, X_train.shape[-1])
probability = model.predict(new_sequence)
print(f"Probability of price going up: {probability[0][0]}")
