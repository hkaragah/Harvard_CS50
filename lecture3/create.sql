CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

/* Other contraints:
    - UNIQUE
    - DEFAULT <0>
    - CHECK <conditions>
*/


