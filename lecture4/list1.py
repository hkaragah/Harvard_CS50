# This file is Flask equivalent of list0.py

import os

from flask import Flask, app, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("HARVARD_CS50_LECTURE4_DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # Tie this database to this Flask app

def main():
    flights = Flight.query.all() # Equivalent to running SELECT * FROM flights, return a list of Flight objects
    for flight in flights:
        print(f"Flight from {flight.origin} to {flight.destination} lasting {flight.duration} minutes.")
        
if __name__ == "__main__":
    with app.app_context(): # Allow us to interact with the Flask app on the "command line"
        main()
        
        
"""
Other commond queries:

SQL: SELECT * FROM flights WHERE origin = "Paris" LIMIT 1;
FLASK: flight = Flight.query.filter_by(origin="Paris").first()

SQL: SELECT COUNT(*) FROM flights WHERE origin = "Paris";
FLASK: Flight.query.filter_by(origin="Paris").count()

SQL: SELECT * FROM flights WHERE id = 28;
FLASK: flight = Flight.query.get(28)
FLASK: flight = Flight.query.filter_by(id=28).first()

SQL: UPDATE flights SET duration = 280 WHERE id = 6;
FLASK: flight = Flight.query.get(6)
       flight.duration = 280
       
SQL DELETE FROM flights WHERE id = 28;
FLASK: flight = Flight.query.get(28)
       db.session.delete(flight)
       
SQL: COMMIT;
FLASK: db.session.commit()

SQL: SELECT * FROM flights ORDER BY origin;
FLASK: flights = Flight.query.order_by(Flight.origin).all()

SQL: SELECT * FROM flights ORDER BY origin DESC;
FLASK: flights = Flight.query.order_by(Flight.origin.desc()).all()

SQL: SELECT * FROM flights WHERE origin != "Paris";
FLASK: flights = Flight.query.filter(Flight.origin != "Paris").all()

SQL: SELECT * FROM flights WHERE origin LIKE "%a%";
FLASK: flights = Flight.query.filter(Flight.origin.like("%a%")).all()

SQL: SELECT * FROM flights WHERE origin IN ("Tokyo", "Paris");
FLASK: flights = Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()

SQL: SELECT * FROM flights WHERE origin = "Paris" AND duration > 500;
FLASK: flights = Flight.query.filter(and_(Flight.origin == "Paris", Flight.duration > 500)).all()

SQL: SELECT * FROM flights WHERE origin = "Paris" OR duration > 500;
FLASK: flights = Flight.query.filter(or_(Flight.origin == "Paris", Flight.duration > 500)).all()

SQL: SELECT * FROM flights JOIN passengers ON flights.id = passengers.flight_id;
FLASK: flights = Flight.query.join(Passenger).filter(Passenger.flight_id == Flight.id).all()
"""
