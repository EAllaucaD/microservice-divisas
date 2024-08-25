from flask import Flask, request, render_template  # Import necessary classes from Flask
import requests  # Import the requests library for making HTTP requests
from dotenv import load_dotenv  # Import the load_dotenv function from dotenv
import os  # Import the os module to work with environment variables and the operating system

app = Flask(__name__)  # Create an instance of the Flask application
load_dotenv()  # Load environment variables from the .env file

API_KEY = os.getenv('API_KEY')  # Retrieve API_KEY from environment variables
URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'  # API URL to fetch exchange rates

def get_rates():
    """Function to fetch exchange rates from the API."""
    response = requests.get(URL)  # Make a GET request to the API URL
    data = response.json()  # Convert the response to JSON format

    if response.status_code != 200:
        return None  # Return None if the request was not successful

    return data['conversion_rates']  # Return the conversion rates obtained from the API

@app.route('/')
def index():
    """Main route that renders the index.html template."""
    return render_template('index.html')  # Render the index.html template

@app.route('/convert', methods=['POST'])
def convert():
    """Route to perform currency conversion."""
    amount = float(request.form['amount'])  # Get the amount to convert from the form
    from_currency = request.form['from_currency']  # Get the source currency from the form
    to_currency = request.form['to_currency']  # Get the target currency from the form
    rates = get_rates()  # Get the exchange rates from the API

    if rates:
        if from_currency != 'USD':
            amount = amount / rates[from_currency]  # Convert amount to USD if it's not USD
        result = amount * rates[to_currency]  # Perform the currency conversion
        return render_template('index.html', result=f'{amount} {from_currency} equals {result:.2f} {to_currency}')
    else:
        return render_template('index.html', error='Error fetching exchange rates')  # Render the template with an error message if exchange rates were not obtained

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the Flask application on host 0.0.0.0 and port 5000 if executed directly
