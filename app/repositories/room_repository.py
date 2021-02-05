from db.run_sql import run_sql
from models.room import Room
import repositories.room_repository as room_repository

def save(room):
    sql = "INSERT INTO rooms (room_number) VALUES (%s) RETURNING id"
    values = [room.room_number]
    results = run_sql(sql, values)
    id = results[0]['id']
    room.id = id

def select_all():
    rooms = []
    sql = "SELECT * FROM rooms"
    results = run_sql(sql)
    for result in results:
        room = Room(result['room_number'], result['id'])
        rooms.append(room)
    return rooms

def select(id):
    sql = "SELECT * FROM rooms WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    room = Room(result['room_number'], result['id'])
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
    