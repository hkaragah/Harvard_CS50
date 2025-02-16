import os

from flask import Flask, app, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("HARVARD_CS50_LECTURE4_DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # Tie this database to this Flask app

@app.route('/')
def index():
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""
    
    # Get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")
    
    # Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such a flight with that id.")
  
    
    # Add passenger
    flight.add_passenger(name)
    return render_template("success.html")



@app.route("/flights")
def flights():
    """Lists all flights."""
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """Lists details about a single flight."""
    
    # Make sure flight exisits.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")
    
    # Get all passengers.
    passengers = flight.passengers # passengers is a property of the Flight class, unlike airline3, we don't need to query the database to get the passengers
    return render_template("flight.html", flight=flight, passengers=passengers)

    
if __name__ == '__main__':
    app.run(debug=False)