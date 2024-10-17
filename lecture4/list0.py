import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("HARVARD_CS50_LECTURE4_DB_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute(text("SELECT origin, destination, duration FROM flights")).fetchall()
    for flight in flights:
        print(f"Flight from {flight.origin} to {flight.destination} lasting {flight.duration} minutes.")
        
if __name__ == "__main__":
    main()