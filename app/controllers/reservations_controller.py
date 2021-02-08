from flask import Flask, redirect, render_template, request, Blueprint

from models.reservation import Reservation
from models.guest import Guest
import repositories.reservation_repository as reservation_repository
import repositories.room_repository as room_repository
import repositories.guest_repository as guest_repository

reservations_blueprint = Blueprint("reservations", __name__)

# All reservations
@reservations_blueprint.route('/reservations')
def reservations():
    reservations = reservation_repository.select_all()
    return render_template('reservations/reservation.html', reservations=reservations)

# Arrivals
@reservations_blueprint.route('/reservations/arrivals')
def arrivals():
    reservations = reservation_repository.arrivals()
    return render_template('reservations/arrival.html', reservations=reservations)

# NEW
@reservations_blueprint.route('/reservations/new')
def new_reservation():
    guests = guest_repository.select_all()
    rooms = room_repository.select_available()
    return render_template('reservations/new.html', guests=guests, rooms=rooms)

# CREATE
@reservations_blueprint.route('/reservations', methods=['POST'])
def create_reservation():
    guest_id = request.form['guest_id']
    guest = guest_repository.select(guest_id)
    room_id = request.form['room_id']
    room = room_repository.select(room_id)
    arrival_date = request.form['arrival_date']
    departure_date = request.form['departure_date']
    status = request.form['status']
    new_reservation = Reservation(guest, room, arrival_date, departure_date, status)
    reservation_repository.save(new_reservation)
    return redirect('/reservations')

# EDIT
@reservations_blueprint.route('/reservations/<id>/edit')
def edit_reservation(id):
    reservation = reservation_repository.select(id)
    guests = guest_repository.select_all()
    rooms = room_repository.select_all()
    return render_template('reservations/edit.html', reservation=reservation, guests=guests, rooms=rooms)

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
    return redirect('/reservations')

# DELETE
@reservations_blueprint.route('/reservations/<id>/delete', methods=['POST'])
def delete_reservation(id):
    reservation_repository.delete(id)
    return redirect('/reservations')

# In House
@ reservations_blueprint.route('/reservations/inhouse')
def show_in_house():
    reservations = reservation_repository.in_house()
    return render_template('reservations/inhouse.html', reservations=reservations)

# Check In
@reservations_blueprint.route('/reservations/<id>/checkin')
def check_in(id):
    reservation = reservation_repository.select(id)
    guest = guest_repository.select(reservation.guest.id)
    rooms = room_repository.select_available()
    return render_template('reservations/checkin.html', reservation=reservation, guest= guest, rooms=rooms)

@reservations_blueprint.route('/reservations/<id>/checkin', methods=['POST'])
def confirm(id):
    res = reservation_repository.select(id)
    room = room_repository.select(res.room.id)
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