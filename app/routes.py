from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('models/trained_model.pkl')

@app.route('/')
def index():
    return 'Welcome to the Diabetes Prediction API'

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the POST request
    data = request.json
    
    # Extract features from the data
    features = [data['Pregnancies'], data['Glucose'], data['BloodPressure'],
                data['SkinThickness'], data['Insulin'], data['BMI'],
                data['DiabetesPedigreeFunction'], data['Age']]
    
    # Make prediction
    prediction = model.predict([features])[0]
    
    # Return the prediction as JSON response
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)
