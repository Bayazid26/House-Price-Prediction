# 🏠 House Price Prediction ML Project

## 🔥 Overview
This is a Machine Learning project that predicts house prices based on features like size, number of bedrooms, and age of the house. It demonstrates a complete end-to-end ML workflow including data preprocessing, model training, evaluation, and deployment using Streamlit.

## 🧠 Tech Stack
Python, NumPy, pandas, scikit-learn, Streamlit, joblib

## 🎯 Objective
Build a system that:
- Takes user input (house features)
- Processes data using a trained ML model
- Predicts house price accurately
- Provides an interactive web interface

## 🤖 Machine Learning Model
Algorithm: Linear Regression  
Type: Supervised Learning (Regression)  
Why: Simple, fast, interpretable, and works well for baseline prediction tasks.

## 📂 Project Structure
house-price-ml-project/
│
├── data/ (housing.csv dataset)
├── src/
│   ├── data_preprocessing.py
│   ├── model.py
│   ├── train.py
│   └── predict.py
├── app.py (Streamlit web app)
├── model.pkl (saved model)
├── requirements.txt
└── README.md

## 📊 Dataset
- size_sqft → House size
- bedrooms → Number of rooms
- age → Age of house
- price → Target variable

## ⚙️ Installation & Setup
Clone repo:
git clone https://github.com/your-username/House-Price-Prediction.git  
cd House-Price-Prediction  

Create virtual environment:
python -m venv venv  

Activate:
Windows:
venv\Scripts\activate  
Mac/Linux:
source venv/bin/activate  

Install dependencies:
pip install -r requirements.txt  

## 🏋️ Train Model
Run:
python src/train.py  

Steps performed:
- Load dataset using pandas
- Split features and target
- Train Linear Regression model
- Evaluate model performance
- Save model as model.pkl

## 🌐 Run Web App
streamlit run app.py  

Then open:
http://localhost:8501  

## 🧪 How It Works
User enters:
- House size
- Bedrooms
- Age  

System:
- Converts input into NumPy array
- Loads trained model
- Predicts house price
- Shows result in UI

## 💡 Example Prediction
Input:
Size: 1500 sqft  
Bedrooms: 3  
Age: 10 years  

Output:
Predicted Price: $300,000+

## 📦 Requirements
pandas  
numpy  
scikit-learn  
streamlit  
joblib  

## 🚀 Features
✔ End-to-end ML pipeline  
✔ Clean modular code  
✔ Data preprocessing with pandas  
✔ Model training using scikit-learn  
✔ Model saving/loading with joblib  
✔ Interactive Streamlit UI  
✔ Beginner-friendly but professional structure  

## 👨‍💻 Author
Your Name  
GitHub: https://github.com/your-username  

## ⭐ Support
If you like this project, star the repository ⭐ and share it 🚀
