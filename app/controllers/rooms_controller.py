from flask import Flask, redirect, render_template, request, Blueprint

from models.room import Room
import repositories.room_repository as room_repository
import repositories.reservation_repository as reservation_repository

rooms_blueprint = Blueprint("rooms", __name__)

# INDEX
@rooms_blueprint.route('/rooms')
def rooms():
    rooms = room_repository.select_all()
    return render_template('rooms/room.html', rooms=rooms)

# NEW
@rooms_blueprint.route('/rooms/new')
def new_room():
    return render_template('rooms/new.html')

# CREATE
@rooms_blueprint.route('/rooms', methods=['POST'])
def create_room():
    number = request.form['number']
    new_room = Room(number)
    room_repository.save(new_room)
    return redirect('/rooms')

# EDIT
@rooms_blueprint.route('/rooms/<id>/edit')
def edit_room(id):
    room = room_repository.select(id)
    return render_template('rooms/edit.html', room=room)

# UPDATE
@rooms_blueprint.route('/rooms/<id>', methods=['POST'])
def update_room(id):
    number = request.form['number']
    updated_room = Room(number, id)
    room_repository.update(updated_room)
    return redirect('/rooms')

# DELETE
@rooms_blueprint.route('/rooms/<id>/delete', methods=['POST'])
def delete_room(id):
    room_repository.delete(id)
    return redirect('/rooms')