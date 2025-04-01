Diabetes Progression Prediction App

Diabetes Prediction Demo
![Diabetes Prediction Demo](demo.gif)

Description

The Diabetes Progression Prediction App is a Machine Learning with FastAPI web application that predicts diabetes progression using a RandomForestRegressor trained on the scikit-learn Diabetes dataset. It features a BMI calculator for normalized input and a user-friendly interface.

Installation and Usage

Clone the Repository

git clone https://github.com/SumanKoo7/FastAPI-for-ML.git
cd diabetes-progression-prediction

Install Dependencies

pip install fastapi uvicorn scikit-learn jinja2 joblib numpy

Train the Model

python model_training.py

Run the App

python app.py

Access the App

Open your browser and go to: http://127.0.0.1:8000

How to Use

BMI Calculator: Enter weight (kg) and height (m), then copy the normalized BMI.

Prediction: Input normalized values (-0.1 to 0.1) for age, sex, BMI, blood pressure, and cholesterol, then click "Predict".

