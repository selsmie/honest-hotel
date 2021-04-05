from db.run_sql import run_sql
from models.guest import Guest
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
        guest = Guest(row['name'], row['stays'], row['preferences'], row['id'])
        guests.append(guest)
    return guests

def select(id):
    guest = None 
    sql = "SELECT * FROM guests WHERE id = %s"
    values =[id]
    result = run_sql(sql, values)[0]
    if result is not None:
        guest = Guest(result['name'], result['stays'], result['preferences'], result['id'])
    return guest

def delete_all():
    sql = "DELETE FROM guests"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM guests WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(guest):
    sql = "UPDATE guests SET (name, preferences) = (%s, %s) WHERE id = %s"
    values = [guest.name, guest.preferences, guest.id]
    run_sql(sql, values)
    print(guest.preferences)

def stays(id):
    # take in reservation id
    # convert id to full reservation details
    res = reservation_repository.select(id)
    # take the reservation's guest id and use to generate full guest details
    guest = guest_repository.select(res.guest.id)
    # use full guest instance with class method to increase stay increase_stay_count
    guest.increase_stay_count()
    # update sql with the guest instance stay count and id as a filter
    sql = "UPDATE guests SET stays = %s WHERE id = %s"
    values = [guest.stays, guest.id]
    run_sql(sql, values)

def search(name):
    guest = None
    sql = "SELECT * FROM guests WHERE name LIKE %s"
    values = [name]
    result = run_sql(sql, values)[0]
    if result is not None:
        guest = Guest(result['name'], result['stays'], result['preferences'], result['id'])
    return guest
