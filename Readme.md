# Bangalore House Price Prediction

# Overview
This project focuses on predicting house prices in Bangalore using machine learning. The dataset consists of various features like location, total square feet, number of bedrooms, bathrooms, etc. The model leverages data preprocessing and regression techniques to provide accurate predictions.

## Dataset
The dataset used in this project contains various real estate features including:
- Location
- Size (BHK)
- Square feet area
- Number of bathrooms
- Price

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-Learn
- Flask (for deployment)

## Project Structure
```
|-- data/                   # Contains dataset files
|-- notebooks/              # Google colab for EDA and model training
|-- static/                 # CSS and JavaScript files (if needed)
|-- templates/              # HTML files for Flask UI
|-- main.py                  # Main Flask application file
|-- README.md               # Project documentation
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/levishsaini/bangalore_price_prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd bangalore_price_prediction
   ```
3. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Google Colab to explore data and train the model.
2. Execute the Flask app for deployment:
   ```bash
   python main.py
   ```
3. Open the browser and go to:
   ```
   http://127.0.0.1:5000/
   ```
   to use the web interface for predictions.

## Model Performance
- Evaluated using metrics like R² score.
- Applied feature engineering and outlier removal for better accuracy.

## Future Enhancements
- Improve model accuracy with advanced regression techniques.
- Deploy the model using cloud services like AWS/GCP.
- Develop an interactive UI for better user experience.

## Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## License
This project is open-source and available under the MIT License.

## Contact
For any inquiries, connect with me on [LinkedIn](https://www.linkedin.com/in/levishkumar/).


