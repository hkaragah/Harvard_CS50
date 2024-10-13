import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("HARVARD_CS50_DB_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    # List all flights
    flights = db.execute(text("SELECT id, origin, destination, duration FROM flights")).fetchall()   
    for flight in flights:
        print(f"flight {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minutes.")
        
    # Promp user to choose a flight
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute(text("SELECT origin, destination, duration FROM flights WHERE id= :id"),
                        {"id": flight.id}).fetchone()
    
    # Make sure flight is valid
    if flight is None:
        print("Error: No such flight.")
        return
    
    # List passengers
    passengers = db.execute(text("SELECT name FROM passengers WHERE flight_id=:flight_id"),
                            {"flight_id":flight_id}).fetchall()
    
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers)==0:
        print("No passengers.")

if __name__ == "__main__":
    main()
        