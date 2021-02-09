from db.run_sql import run_sql
from models.reservation import Reservation
from models.guest import Guest
from models.room import Room
import repositories.room_repository as room_repository
import repositories.guest_repository as guest_repository

def save(reservation):
    sql = "INSERT INTO reservations (guest_id, room_id, arrival_date, departure_date, status) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [reservation.guest.id, reservation.room.id, reservation.arrival_date, reservation.departure_date, reservation.status]
    results = run_sql(sql, values)
    reservation.id = results[0]['id']
    return reservation

def select_all():
    reservations = []
    sql = "SELECT * FROM reservations ORDER BY arrival_date, status ASC"
    results = run_sql(sql)
    for row in results:
        guest = guest_repository.select(row['guest_id'])
        room = room_repository.select(row['room_id'])
        reservation = Reservation(guest, room, row['arrival_date'], row['departure_date'], row['status'], row['id'])
        reservations.append(reservation)
    return reservations

def select(id):
    reservation = None
    sql = "SELECT * FROM reservations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        guest = guest_repository.select(result['guest_id'])
        room = room_repository.select(result['room_id'])
        reservation = Reservation(guest, room, result['arrival_date'], result['departure_date'], result['status'], result['id'])
    return reservation

def delete(id):
    sql = "DELETE FROM reservations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(reservation):
    sql = "UPDATE reservations SET (guest_id, room_id, arrival_date, departure_date, status) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [reservation.guest.id, reservation.room.id, reservation.arrival_date, reservation.departure_date, reservation.status, reservation.id]
    run_sql(sql, values)

def arrivals():
    reservations = []
    sql = "SELECT * FROM reservations WHERE arrival_date = %s AND status = %s ORDER BY arrival_date ASC"
    values = ["2021-02-11", "Arrival"]
    results = run_sql(sql, values)
    for row in results:
        guest = guest_repository.select(row['guest_id'])
        room = room_repository.select(row['room_id'])
        reservation = Reservation(guest, room, row['arrival_date'], row['departure_date'], row['status'], row['id'])
        reservations.append(reservation)
    return reservations


def in_house():
    reservations = []
    sql = "SELECT * FROM reservations WHERE status = %s ORDER BY room_id"
    values = ["Checked In"]
    results = run_sql(sql, values)
    for row in results:
        guest = guest_repository.select(row['guest_id'])
        room = room_repository.select(row['room_id'])
        reservation = Reservation(guest, room, row['arrival_date'], row['departure_date'], row['status'], row['id'])
        reservations.append(reservation)
    return reservations

def check_in(id):
    sql = "UPDATE reservations SET status = %s WHERE id = %s"
    values = ["Checked In", id]
    run_sql(sql, values)

def check_out(id):
    sql = "UPDATE reservations SET status = %s WHERE id = %s"
    values = ["Departed", id]
    run_sql(sql, values)

def update_room(room, id):
    sql = "UPDATE reservations SET room_id = %s WHERE id = %s"
    values = [room.id, id]
    run_sql(sql, values)

def total_arrivals():
    arrivals = 0
    sql = "SELECT * FROM reservations WHERE arrival_date = %s AND status = %s"
    values = ['2021-02-11', "Arrival"]
    results = run_sql(sql, values)
    for row in results:
        arrivals += 1
    return arrivals

def total_departures():
    departures = 0
    sql = "SELECT * FROM reservations WHERE departure_date = %s AND status = %s"
    values = ['2021-02-11', "Checked In"]
    results = run_sql(sql, values)
    for row in results:
        departures += 1
    return departures

def total_inh_rooms():
    rooms = 0
    sql = "SELECT * FROM reservations WHERE status = %s"
    values = ["Checked In"]
    results = run_sql(sql, values)
    for row in results:
        rooms += 1
    return rooms

def current_occupancy():
    total_rooms = len(room_repository.select_all()) - 1
    print(total_rooms)
    inh = total_inh_rooms()
    current_occupancy = (inh/ total_rooms) * 100
    return round(current_occupancy, 1)

def expected_occupancy():
    total_rooms = len(room_repository.select_all()) - 1
    print(total_rooms)
    inh = total_inh_rooms()
    expected_occupancy = ((inh - total_departures() + total_arrivals()) / total_rooms) * 100
    return round(expected_occupancy, 1)