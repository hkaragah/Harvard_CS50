import csv
import os

from git import Commit
from sqlalchemy import create_engine, text
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("HARVARD_CS50_DB_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    with open("flights.csv", "r") as f:
        reader = csv.reader(f)
        for origin, destination, duration in reader:
            db.execute(text("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)"),
                            {"origin":origin, "destination":destination, "duration":duration})
            print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
        db.commit() # to avoid "Race Conditions"
            
if __name__ == "__main__":
    main()