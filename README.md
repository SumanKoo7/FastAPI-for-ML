# 🩺 Diabetes Progression Prediction App

## 🚀 Overview
The **Diabetes Progression Prediction App** is a FastAPI-based web application that predicts diabetes progression using a `RandomForestRegressor` trained on the scikit-learn Diabetes dataset. It includes a BMI calculator for input normalization and a modern, user-friendly interface.

## 📷 Demo
![Demo](https://github.com/user-attachments/assets/82ccb15e-fc1b-4d0c-9949-6daa296c9797)

## 🛠 Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SumanKoo7/FastAPI-for-ML.git
cd diabetes-progression-prediction
```
### 2️⃣ Install Dependencies
```bash
pip install fastapi uvicorn scikit-learn jinja2 joblib numpy
```
### 3️⃣ Train the Model
```bash
python model_training.py
```
### 4️⃣ Run the App
```bash
python app.py
```
### 5️⃣ Access the App
Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🎯 How to Use
1. **BMI Calculator**: Enter weight (kg) and height (m), then copy the normalized BMI.
2. **Make a Prediction**: Input normalized values (-0.1 to 0.1).
3. Click **"Predict"** to get the diabetes progression estimate.

## 📝 License
This project is open-source and available under the MIT License.

### 🌟 If you find this project useful, don't forget to **star ⭐ the repository!**
