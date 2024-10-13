import os

from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker


# # Retrieve the username, password, and database from environment variables
# user = os.getenv("PGUSER")
# password = os.getenv("PGPASSWORD")
# host = "localhost"  # Assuming PostgreSQL is running locally
# port = "5432"       # Default port for PostgreSQL
# dbname = os.getenv("PGDATABASE")  # Optionally set this in the environment too


# # Construct the connection URL without hardcoding credentials
# db_url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
# engine = create_engine(db_url)

engine = create_engine(os.getenv("HARVARD_CS50_DB_URL"))
db = scoped_session(sessionmaker(bind=engine)) # create different sessions for different users

def main():
    flights = db.execute(text("SELECT origin, destination, duration FROM flights"))
    
    # If we want the result to return as a list
    # flights = db.execute(text("SELECT origin, destination, duration FROM flights")).fetchall()
    
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.") 
        
if __name__ == "__main__":
    main()