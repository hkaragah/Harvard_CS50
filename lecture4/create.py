import os

from flask import Flask, app, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app) # Tie this database to this Flask app

def main():
    # Create tables based on each class that inherits from db.Model
    db.create_all()
    
if __name__ == "__main__":
    with app.app_context(): # Allow us to interact with the Flask app on the "command line"
        main()