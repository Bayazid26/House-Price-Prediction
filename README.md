🏠 House Price Prediction ML Project
🔥 Overview

This project predicts house prices using Machine Learning (Linear Regression).
It is built using Python and demonstrates a full ML workflow including data processing, model training, and deployment using Streamlit.

🧠 Tech Stack
Python 🐍
NumPy 🔢
pandas 📊
scikit-learn 🤖
Streamlit 🌐
📂 Project Structure
src/          → Source code (ML pipeline)
data/         → Dataset (CSV file)
app.py        → Streamlit web app
model.pkl     → Saved trained model
requirements.txt → Dependencies
🚀 How to Run
1. Install dependencies

First, install all required libraries:

pip install -r requirements.txt

👉 This installs:

pandas → for data handling
numpy → for numerical operations
scikit-learn → for machine learning model
streamlit → for web app interface
joblib → for saving/loading model
2. Train the model

Run the training script:

python src/train.py

✔ This will:

Load dataset from data/housing.csv
Split data into training/testing sets
Train Linear Regression model
Evaluate model performance
Save model as model.pkl
3. Run the web application

Start Streamlit app:

streamlit run app.py

Then open in browser:

http://localhost:8501
🧪 How It Works
User enters:
House size (sqft)
Number of bedrooms
Age of house
Model processes input using trained regression model
Output is predicted house price 💰
📊 Example Prediction
Input	Value
Size	1500 sqft
Bedrooms	3
Age	10 years
👉 Output:
Predicted Price: $300,000+
📦 Requirements
pandas
numpy
scikit-learn
streamlit
joblib
🚀 Features

✔ Simple ML pipeline
✔ Clean dataset handling
✔ Model training & evaluation
✔ Model saving (joblib)
✔ Interactive UI using Streamlit
✔ Beginner-friendly project

🔮 Future Improvements
Add more features (location, city, etc.)
Use advanced models (Random Forest / XGBoost)
Use real Kaggle dataset
Improve UI design
Deploy on cloud (Render / AWS / Streamlit Cloud)
