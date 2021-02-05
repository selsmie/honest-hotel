DROP TABLE IF EXISTS reservations;
DROP TABLE IF EXISTS rooms;
DROP TABLE IF EXISTS guests;

CREATE TABLE guests (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE rooms (
    id SERIAL PRIMARY KEY,
    room_number INT
);

CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    guest_id INT REFERENCES guests(id) ON DELETE CASCADE,
    room_id INT REFERENCES rooms(id) ON DELETE CASCADE
);