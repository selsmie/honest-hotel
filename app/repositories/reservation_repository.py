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

    sql = "SELECT * FROM reservations ORDER BY arrival_date"
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

    sql = "SELECT * FROM reservations WHERE status = %s"
    values = ["Incoming"]
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
    guest = guest_repository.select(id)
    guest.increase_stay_count()
    stays = guest.stays
    sql = "UPDATE guests SET stays = %s WHERE id = %s"
    values = [stays, id]
    run_sql(sql, values)
    sql = "UPDATE reservations SET status = %s WHERE id = %s"
    values = ["Departed", id]
    run_sql(sql, values)
    
    


