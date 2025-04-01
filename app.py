from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.datasets import load_diabetes

# Load the trained model
model = joblib.load("diabetes_model.pkl")

# Initialize FastAPI
app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

# Pydantic model for input data
class DiabetesInput(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float  # total serum cholesterol

class DiabetesPrediction(BaseModel):
    predicted_progression: float

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_model=DiabetesPrediction)
async def predict(
    request: Request,
    age: float = Form(...),
    sex: float = Form(...),
    bmi: float = Form(...),
    bp: float = Form(...),
    s1: float = Form(...),
):
    # Create full feature array with zeros for unused features
    input_data = np.zeros(10)
    input_data[0] = age
    input_data[1] = sex
    input_data[2] = bmi
    input_data[3] = bp
    input_data[4] = s1
    input_data = input_data.reshape(1, -1)

    # Make prediction
    predicted_progression = float(model.predict(input_data)[0])

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "predicted_progression": predicted_progression,
            "age": age,
            "sex": sex,
            "bmi": bmi,
            "bp": bp,
            "s1": s1
        },
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)