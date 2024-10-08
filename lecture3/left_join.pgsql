SELECT origin, destination, name 
FROM flights 
LEFT JOIN passengers 
    ON passengers.flight_id=flights.id;