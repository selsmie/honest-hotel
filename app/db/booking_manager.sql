DROP TABLE IF EXISTS reservations;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS guests;

CREATE TABLE guests (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    stays INT
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    room_number INT,
    remaining_capacity INT
);

CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    guest_id INT REFERENCES guests(id) ON DELETE CASCADE,
    room_id INT REFERENCES rooms(id),
    arrival_date DATE NOT NULL,
    departure_date DATE NOT NULL,
    status VARCHAR(255)
);