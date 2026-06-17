import joblib
import numpy as np

model = joblib.load("model.pkl")

def predict_price(size_sqft, bedrooms, age):
    input_data = np.array([[size_sqft, bedrooms, age]])
    prediction = model.predict(input_data)
    return prediction[0]

if __name__ == "__main__":
    print(predict_price(1500, 3, 10))