
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def currency():
    # Query for currency exchange rate
    currency = request.form.get('currency')
    # res = requests.get(
    #     'http://api.fixer.io/latest',
    #     params={'base': 'USD', 'symbols': currency}
    # )
    
    res = requests.get(
        'https://open.er-api.com/v6/latest/USD'
    )
    



    # res = requests.get(
    #     'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_vsbtgONP1s9dxH9vKXcaGPLJLZ2Z0BQjtjakD3pS'
    # )
    # The above API's response has the following structure:
    # "data": {
    #     "EUR": 0.9592001342,
    #     "GBP": 0.8108901305,
    #     "USD": 1,
    # }
    # Change the following lines accordingly
    
    
    
    
    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({'success': False})
    
    # Make sure currency is in response
    data = res.json()
    if currency not in data['rates']:
        return jsonify({'success': False})
    
    return jsonify({
        'success': True,
        'rate': data['rates'][currency]
    })