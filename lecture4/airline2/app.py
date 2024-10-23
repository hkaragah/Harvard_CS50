import sys
import os

# Add the directory containing the module to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, app, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("HARVARD_CS50_LECTURE4_DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # Tie this database to this Flask app

@app.route('/')
def index():
    # SQL version: flights = db.execute(text("SELECT * FROM flights")).fetchall()
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
    """
    SQL version:
    if db.execute(text("SELECT * FROM flights WHERE id=:id"), {"id":flight_id}).rowcount==0:
        return render_template("error.html", message="No such a flight with that id.")
    """   
    
    # Add passenger
    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template("success.html")
    """
    SQL version:
    db.execute(text("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)"),
                {"name": name, "flight_id": flight_id})
    db.commit()
    return render_template("success.html")
    """


@app.route("/flights")
def flights():
    """Lists all flights."""
    # SQL version: flights = db.execute(text("SELECT * FROM flights")).fetchall()
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """Lists details about a single flight."""
    
    # Make sure flight exisits.
    # SQL version: flight = db.execute(text("SELECT * FROM flights WHERE id=:id"), {"id": flight_id}).fetchone()
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")
    
    # Get all passengers.
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template("flight.html", flight=flight, passengers=passengers)
    """
    SQL version:
        passengers = db.execute(text("SELECT * FROM passengers WHERE flight_id=:flight_id"),
                            {"flight_id": flight_id}).fetchall()
    return render_template("flight.html", flight=flight, passengers=passengers)
    """
    
if __name__ == '__main__':
    app.run(debug=False)