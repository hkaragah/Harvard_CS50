UPDATE flights
    SET duration = 430
    /* or SET duration = duration - 10 */
    WHERE origin = 'New York' AND destination = 'London';