import joblib
import numpy as np

# Load trained model
model = joblib.load("linear_regression_model.pkl")

print("Enter 8 feature values separated by commas:")
print("Format: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude")

values = list(map(float, input().split(",")))

prediction = model.predict([values])
print("Predicted Median House Value:", prediction[0])
