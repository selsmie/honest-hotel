from db.run_sql import run_sql
from models.guest import Guest

def save(guest):
    sql = "INSERT INTO guests (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [guest.first_name, guest.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    guest.id = id

def select_all():
    guests = []
    sql = "SELECT * FROM guests"
    results = run_sql(sql)
    for result in results:
        guest = Guest(result['first_name'], result['last_name'], result['id'])
        guests.append(guest)
    return guests

def select(id):
    sql = "SELECT * FROM guests WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]
    guest = Guest(result['first_name'], result['last_name'], result['id'])
    return Guest

def delete_all():
    sql = "DELETE FROM guests"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM guests WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(guest):
    sql = "UPDATE guests SET (first_name, last_name) = (%s, %s) WHERE id = %s"
    values = [guest.first_name, guest.last_name, guest.id]
    run_sql(Sql, values)