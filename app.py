import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("🏠 House Price Prediction App")

st.write("Enter house details below:")

size = st.number_input("Size (sqft)", min_value=0)
bedrooms = st.number_input("Bedrooms", min_value=1)
age = st.number_input("Age of house", min_value=0)

if st.button("Predict Price"):
    input_data = np.array([[size, bedrooms, age]])
    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Price: ${prediction:,.2f}")