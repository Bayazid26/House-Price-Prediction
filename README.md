# 🏠 House Price Prediction ML Project

## 🔥 Overview

This project is a **Machine Learning application** that predicts house prices based on key features such as:

- 📏 Size of the house (square feet)
- 🛏️ Number of bedrooms
- 🏚️ Age of the house

The project demonstrates a complete **end-to-end ML workflow**, including:

- Data preprocessing using pandas
- Numerical computation using NumPy
- Model building using scikit-learn
- Model evaluation
- Model saving/loading
- Web deployment using Streamlit

This is a **beginner-friendly but portfolio-ready project** suitable for GitHub and internships.

---

## 🎯 Project Objective

The main goal is to build a system that can:

✔ Take user input (house features)  
✔ Process data using trained ML model  
✔ Predict house price accurately  
✔ Provide interactive web interface  

---

## 🧠 Machine Learning Approach

- **Algorithm Used:** Linear Regression  
- **Type:** Supervised Learning (Regression Problem)  
- **Library:** scikit-learn  

### Why Linear Regression?

Linear Regression is used because:
- It is simple and interpretable
- Works well for small datasets
- Provides a strong baseline model

---

## 📂 Project Structure
house-price-ml-project/
│
├── data/
│ └── housing.csv # Dataset file
│
├── src/
│ ├── data_preprocessing.py # Data loading & preprocessing
│ ├── model.py # Model definition
│ ├── train.py # Training script
│ └── predict.py # Prediction script
│
├── app.py # Streamlit web app
├── model.pkl # Saved trained model
├── requirements.txt # Dependencies
├── README.md # Documentation
└── .gitignore # Ignored files


---

## 📊 Dataset Information

The dataset contains simple housing data:

| Feature     | Description              |
|-------------|--------------------------|
| size_sqft   | Size of house (sqft)     |
| bedrooms    | Number of bedrooms       |
| age         | Age of house (years)     |
| price       | Target variable (price)  |

---

## ⚙️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction



## 2️⃣ Create Virtual Environment
python -m venv venv

Activate environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate
## 3️⃣ Install Dependencies
pip install -r requirements.txt
## 🏋️ Model Training

Run the training script:

python src/train.py
What happens during training:

✔ Dataset is loaded using pandas
✔ Features and target are separated
✔ Data is split into training/testing sets
✔ Linear Regression model is trained
✔ Model is evaluated using metrics
✔ Model is saved as model.pkl

📈 Model Evaluation

The model is evaluated using:

📉 Mean Squared Error (MSE)
📊 R² Score

These metrics help measure prediction accuracy.

##🌐 Run Web Application

Start Streamlit app:

streamlit run app.py


## 🧪 How It Works
Step-by-step flow:
User enters:
House size
Number of bedrooms
Age of house
Data is converted into NumPy array
Trained model predicts price
Result is displayed in web interface

##💡 Example Prediction
Input:
Size: 1500 sqft
Bedrooms: 3
Age: 10 years
Output:
Predicted Price: $300,000+

##📦 Requirements
pandas
numpy
scikit-learn
streamlit
joblib

##🚀 Features
✔ End-to-end ML pipeline
✔ Clean modular code structure
✔ Data preprocessing with pandas
✔ Model training using scikit-learn
✔ Model saving using joblib
✔ Interactive UI using Streamlit
✔ Beginner-friendly but professional design
