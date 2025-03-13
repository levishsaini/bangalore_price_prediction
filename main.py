import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np

# Create a Flask app
app = Flask(__name__)

# Load the data
data = pd.read_csv('Cleaned_data.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None  # Default value for prediction

    # Sorted locations from the data
    locations = sorted(data['location'].unique())
    
    if request.method == 'POST':
        # Get input values from the form
        location = request.form.get('location')
        bhk = request.form.get('bhk')
        bath = request.form.get('bath')
        total_sqft = request.form.get('total_sqft')

        # Convert input values to appropriate types
        bhk = int(bhk)
        bath = int(bath)
        sqft = float(total_sqft)

        # Create a DataFrame for the model input
        input_data = pd.DataFrame([[location, bath, bhk, sqft]], columns=['location', 'bath', 'bhk', 'total_sqft'])

        # Make prediction using the loaded model
        prediction = pipe.predict(input_data)[0] * 1e5

        # Round the prediction to two decimal places
        prediction = np.round(prediction, 2)

        # Return the prediction as a string for AJAX response
        return str(prediction)

    return render_template('index.html', locations=locations, prediction=prediction)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
