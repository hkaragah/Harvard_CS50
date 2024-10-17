# This file is used to import data from a CSV file into a database table.
# This file is another version of import0.py that uses the Flask app context to interact with the database.

import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("HARVARD_CS50_LECTURE4_DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # Tie this database to this Flask app

def main():
    f = open("./lecture4/flights.csv")
    reader = csv.reader(f)
    for origin, destination, duration in reader:
        flight = Flight(origin=origin, destination=destination, duration=duration)
        db.session.add(flight) # Equivalent to running INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit() # Equivalent to running COMMIT
    
if __name__ == "__main__":
    with app.app_context(): # Allow us to interact with the Flask app on the "command line"
        main()