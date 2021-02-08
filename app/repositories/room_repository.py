from db.run_sql import run_sql
from models.room import Room
import repositories.room_repository as room_repository
import repositories.reservation_repository as reservation_repository

import pdb

def save(room):
    sql = "INSERT INTO rooms (room_number, remaining_capacity) VALUES (%s, %s) RETURNING id"
    values = [room.room_number, room.remaining_capacity]
    results = run_sql(sql, values)
    id = results[0]['id']
    room.id = id

def select_all():
    rooms = []
    sql = "SELECT * FROM rooms"
    results = run_sql(sql)
    for result in results:
        room = Room(result['room_number'], result['remaining_capacity'], result['id'])
        rooms.append(room)
    return rooms

def select_available():
    rooms = []
    sql = "SELECT * FROM rooms WHERE remaining_capacity > 0"
    results = run_sql(sql)
    for result in results:
        room = Room(result['room_number'], result['remaining_capacity'], result['id'])
        rooms.append(room)
    return rooms


def select(id):
    room = None
    sql = "SELECT * FROM rooms WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        room = Room(result['room_number'], result['remaining_capacity'], result['id'])
    return room

def delete_all():
    sql = "DELETE FROM rooms"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM rooms WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(room):
    sql = "UPDATE rooms SET room_number = %s WHERE id = %s"
    values = [room.room_number, room.id]
    run_sql(sql, values)
    
def capacity_in(id):
    res = reservation_repository.select(id)
    room = room_repository.select(res.room.id)
    room.capacity_change_in()
    sql = "UPDATE rooms SET remaining_capacity = %s WHERE id = %s"
    values = [room.remaining_capacity, room.id]
    run_sql(sql, values)

def capacity_out(id):
    res = reservation_repository.select(id)
    room = room_repository.select(res.room.id)
    room.capacity_change_out()
    sql = "UPDATE rooms SET remaining_capacity = %s WHERE id = %s"
    values = [room.remaining_capacity, room.id]
    run_sql(sql, values)
