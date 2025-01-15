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
    passengers = db.relationship("Passenger", backref="flight", lazy=True) # not a column in the flight table
    # "passengers" is a property of the Flight class that only exists inside the Python code and is a relationship that connects multiple table together
    # "backref" is a way to access the flight that a passenger is on
    # "lazy" is a way to load the passengers data from the database only when we need it
    
    def add_passenger(self, name):
        p = Passenger(name=name, flight_id=self.id)
        db.session.add(p)
        db.session.commit()
    
    
class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)