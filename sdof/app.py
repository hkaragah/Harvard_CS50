# app.py
from flask import Flask, request, render_template, jsonify
import numpy as np
from math import sqrt, pi

app = Flask(__name__)

def calculate_natural_period(mass, stiffness):
    """
    Calculate the natural period of a SDOF system
    T = 2π√(m/k)
    """
    # Convert inputs to float
    mass = float(mass)
    stiffness = float(stiffness)
    
    # Calculate natural frequency (ω = √(k/m))
    natural_frequency = sqrt(stiffness / mass)
    
    # Calculate natural period (T = 2π/ω = 2π√(m/k))
    natural_period = 2 * pi * sqrt(mass / stiffness)
    
    return {
        'natural_period': round(natural_period, 4),
        'natural_frequency': round(natural_frequency, 4)
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()

        mass = float(data['mass'])
        stiffness = float(data['stiffness'])
        
        if mass <= 0 or stiffness <= 0:
            return jsonify({'error': 'Mass and stiffness must be positive values'}), 400
            
        results = calculate_natural_period(mass, stiffness)
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)