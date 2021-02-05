from db.run_sql import run_sql
from models.reservation import Reservation
from models.guest import Guest
from models.room import Room
import repositories.room_repository as room_repository
import repositories.guest_repository as guest_repository

def save(reservation):
    sql = "INSERT INTO reservations (guest_id, room_id) VALUES (%s, %s) RETURNING id"
    values = [reservation.guest.id, reservation.room.id]
    results = run_sql(sql, values)
    reservation.id = results[0]['id']
    return reservation

def select_all():
    reservations = []

    sql = "SELECT * FROM reservations"
    results = run_sql(sql)

    for row in results:
        guest = guest_repository.select(row['guest_id'])
        room = room_repository.select(row['room_id'])
        reservation = Reservation(guest, room, row['id'])
        reservations.append(reservation)
    return reservations

def select(id):
    reservation = None
    sql = "SELECT * FROM reservations WHERE id = %s"
    value = [id]
    result = run_sql(sql, values)
    if reservation is not None:
        guest = guest_repository.select(result['guest_id'])
        room = room_repository.select(result['room_id'])
        reservation = Reservation[guest, room, result['id']]
    return reservation

def delete(id):
    sql = "DELETE FROM reservations WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(reservation):
    sql = "UPDATE reservations SET (guest_id, room_id) = (%s, %s) WHERE id = %s"
    values = [reservation.guest.id, reservation.room.id, reservation.id]
    run_sql(sql, values)