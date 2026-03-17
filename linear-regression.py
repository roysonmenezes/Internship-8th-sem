# Assignment (09/03/2026)
# Assignment Name: House Price Predictor
# Description: Train a Linear Regression model, predict prices, and test with new input

from sklearn.linear_model import LinearRegression
import numpy as np

# Dataset (House Size in sq.ft vs Price in $1000)
house_size = np.array([[500], [800], [1000], [1200], [1500]])
price = np.array([100, 150, 200, 240, 300])

# Create and train model
model = LinearRegression()
model.fit(house_size, price)

# Predict price for a new house
new_size = np.array([[1100]])
predicted_price = model.predict(new_size)

print("Predicted price for 1100 sq.ft house:", predicted_price[0])