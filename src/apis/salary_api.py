from flask import Blueprint, request, jsonify
import pickle
import pandas as pd

salary_bp = Blueprint('salary_bp', __name__)

# Load the trained model
with open('./models/salary_model.pkl', 'rb') as f:
    salary_model = pickle.load(f)

@salary_bp.route('/predict', methods=['POST'])
def predict_salary():
    data = request.json

    # Expected input fields
    input_df = pd.DataFrame([{
        "years_experience": data.get("years_experience", 0),
        "role": data.get("role", ""),
        "degree": data.get("degree", ""),
        "company_size": data.get("company_size", ""),
        "location": data.get("location", ""),
        "level": data.get("level", "")
    }])

    # Predict
    prediction = salary_model.predict(input_df)

    return jsonify({
        "prediction": float(prediction[0])
    })
