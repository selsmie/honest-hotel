from db.run_sql import run_sql
from models.guest import Guest

def save(guest):
    sql = "INSERT INTO guests (name) VALUES (%s) RETURNING id"
    values = [guest.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    guest.id = id

def select_all():
    guests = []
    sql = "SELECT * FROM guests"
    results = run_sql(sql)
    for row in results:
        guest = Guest(row['name'], row['id'])
        guests.append(guest)
    return guests

def select(id):

    sql = "SELECT * FROM guests WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]

    guest = Guest(result['name'], result['id'])
    return guest

def delete_all():
    sql = "DELETE FROM guests"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM guests WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(guest):
    sql = "UPDATE guests SET (name) = (%s) WHERE id = %s"
    values = [guest.name, guest.id]
    run_sql(sql, values)