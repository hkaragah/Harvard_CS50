from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# For any table in database there is a class in models.py file
class Flight(db.Model):
    
    # Name of the table in the database that this class is going to represent
    __tablename__ = "flights"
    
    # Define columns of the table
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    
    
class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)