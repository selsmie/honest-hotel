from flask import Flask, redirect, render_template, request, Blueprint

from models.reservation import Reservation
from models.guest import Guest
import repositories.reservation_repository as reservation_repository
import repositories.room_repository as room_repository
import repositories.guest_repository as guest_repository
import datetime

reservations_blueprint = Blueprint("reservations", __name__)

# All reservations
@reservations_blueprint.route('/reservations')
def reservations():
    reservations = reservation_repository.select_all()
    reservation_repository.arrival_status()
    today = datetime.date.today()
    return render_template('reservations/reservation.html', reservations=reservations, today=today)

# @reservations_blueprint.route('/reservations', methods=['POST'])
# def reservations_from_today():
#     date = request.form['date']
#     reservations = reservation_repository.select_from_today(date)
#     return render_template('reservations/reservation.html', reservations=reservations)

# Arrivals
@reservations_blueprint.route('/reservations/arrivals')
def arrivals():
    reservations = reservation_repository.arrivals()
    reservation_repository.arrival_status()
    return render_template('reservations/arrival.html', reservations=reservations)

# NEW
@reservations_blueprint.route('/reservations/new')
def new_reservation():
    guests = guest_repository.select_all()
    room = room_repository.select_default()
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)
    return render_template('reservations/new.html', guests=guests, room=room, today=today, tomorrow=tomorrow)

# CREATE
@reservations_blueprint.route('/reservations', methods=['POST'])
def create_reservation():
    guest_id = request.form['guest_id']
    guest = guest_repository.select(guest_id)
    room = room_repository.select_default()
    arrival_date = request.form['arrival_date']
    departure_date = request.form['departure_date']
    status = request.form['status']
    new_reservation = Reservation(guest, room, arrival_date, departure_date, status)
    reservation_repository.save(new_reservation)
    reservation_repository.arrival_status()
    return redirect('/reservations')

# EDIT
@reservations_blueprint.route('/reservations/<id>/edit')
def edit_reservation(id):
    reservation = reservation_repository.select(id)
    guests = guest_repository.select_all()
    rooms = room_repository.select_all()
    today = datetime.date.today()
    stay_length = reservation_repository.stay_length(id)
    return render_template('reservations/edit.html', reservation=reservation, guests=guests, rooms=rooms, today=today, stay_length=stay_length)

# UPDATE
@reservations_blueprint.route('/reservations/<id>', methods=['POST'])
def update_reservation(id):
    guest_id = request.form['guest_id']
    guest = guest_repository.select(guest_id)
    room_id = request.form['room_id']
    room = room_repository.select(room_id)
    arrival_date = request.form['arrival_date']
    departure_date = request.form['departure_date']
    status = request.form['status']
    updated_reservation = Reservation(guest, room, arrival_date, departure_date, status, id)
    reservation_repository.update(updated_reservation)
    reservation_repository.arrival_status()
    return redirect('/reservations')

# DELETE
@reservations_blueprint.route('/reservations/<id>/delete')
def delete_reservation(id):
    reservation = reservation_repository.select(id)
    guest = guest_repository.select(reservation.guest.id)
    return render_template('reservations/delete.html', reservation=reservation, guest= guest)

@reservations_blueprint.route('/reservations/<id>/delete', methods=['POST'])
def delete_confirm(id):
    reservation_repository.delete(id)
    return redirect('/reservations')

# In House
@ reservations_blueprint.route('/reservations/inhouse')
def show_in_house():
    reservations = reservation_repository.in_house()
    reservation_repository.arrival_status()
    today = datetime.date.today()
    return render_template('reservations/inhouse.html', reservations=reservations, today=today)

# Check In
@reservations_blueprint.route('/reservations/<id>/checkin')
def check_in(id):
    reservation = reservation_repository.select(id)
    guest = guest_repository.select(reservation.guest.id)
    rooms = room_repository.select_available()
    stay_length = reservation_repository.stay_length(id)
    return render_template('reservations/checkin.html', reservation=reservation, guest= guest, rooms=rooms, stay_length=stay_length)

@reservations_blueprint.route('/reservations/<id>/checkin', methods=['POST'])
def confirm(id):
    room_id = request.form['room_id']
    assigned_room = room_repository.select(room_id) 
    reservation_repository.update_room(assigned_room, id)
    room_repository.capacity_in(id)
    reservation_repository.check_in(id)
    return redirect('/reservations')

# Check Out
@reservations_blueprint.route('/reservations/<id>/departed')
def check_out(id):
    guest_repository.stays(id)
    reservation_repository.check_out(id)
    room_repository.capacity_out(id)
    return redirect('/reservations')

# Search
@reservations_blueprint.route('/reservations/search', methods=['POST'])
def search_name():
    search_name = request.form['search']
    reservation = reservation_repository.search(search_name.title())
    guests = guest_repository.select_all()
    rooms = room_repository.select_all()
    return render_template('reservations/edit.html', reservation=reservation, guests=guests, rooms=rooms)
    
