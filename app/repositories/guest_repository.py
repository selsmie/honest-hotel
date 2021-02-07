from db.run_sql import run_sql
from models.guest import Guest
import repositories.guest_repository as guest_repository
import repositories.reservation_repository as reservation_repository

def save(guest):
    sql = "INSERT INTO guests (name, stays) VALUES (%s, %s) RETURNING id"
    values = [guest.name, guest.stays]
    results = run_sql(sql, values)
    id = results[0]['id']
    guest.id = id

def select_all():
    guests = []
    sql = "SELECT * FROM guests"
    results = run_sql(sql)
    for row in results:
        guest = Guest(row['name'], row['stays'], row['id'])
        guests.append(guest)
    return guests

def select(id):
    guest = None 
    sql = "SELECT * FROM guests WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]
    if result is not None:
        guest = Guest(result['name'], result['stays'], result['id'])
    return guest

def delete_all():
    sql = "DELETE FROM guests"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM guests WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(guest):
    sql = "UPDATE guests SET name = %s WHERE id = %s"
    values = [guest.name, guest.id]
    run_sql(sql, values)

def stays(id):
    res = reservation_repository.select(id)
    guest = guest_repository.select(res.guest.id)
    guest.increase_stay_count()
    print(guest.stays)
    sql = "UPDATE guests SET stays = %s WHERE id = %s"
    values = [guest.stays, guest.id]
    run_sql(sql, values)

