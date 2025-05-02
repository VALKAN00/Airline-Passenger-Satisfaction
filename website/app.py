from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

# Load the trained model
with open('SVM_grid_search.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the Flask app
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define the expected input columns
COLUMNS = [
    'Gender', 'Customer Type', 'Age', 'Type of Travel', 'Class',
    'Flight Distance', 'Inflight wifi service', 'Departure/Arrival time convenient',
    'Ease of Online booking', 'Gate location', 'Food and drink', 'Online boarding',
    'Seat comfort', 'Inflight entertainment', 'On-board service', 'Leg room service',
    'Baggage handling', 'Checkin service', 'Inflight service', 'Cleanliness',
    'Departure Delay in Minutes', 'Arrival Delay in Minutes'
]

# GET endpoint for checking the API
@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Welcome to the Satisfaction Prediction API. Use the POST /predict endpoint with JSON input."
    })

# POST endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Validate keys
        missing_cols = [col for col in COLUMNS if col not in data]
        if missing_cols:
            return jsonify({'error': f'Missing columns: {missing_cols}'}), 400

        # Convert input to DataFrame
        df = pd.DataFrame([data], columns=COLUMNS)
        
        # Predict
        prediction = model.predict(df)[0]
        return jsonify({'satisfaction': str(prediction)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
