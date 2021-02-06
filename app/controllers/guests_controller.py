from flask import Flask, redirect, render_template, request, Blueprint

from models.guest import Guest
import repositories.guest_repository as guest_repository

guests_blueprint = Blueprint("guests", __name__)

# INDEX
@guests_blueprint.route('/guests')
def guests():
    guests = guest_repository.select_all()
    return render_template('guests/guest.html', guests=guests)

# NEW
@guests_blueprint.route('/guests/new')
def new_guest():
    return render_template('guests/new.html')

# CREATE
@guests_blueprint.route('/guests', methods=['POST'])
def create_guest():
    name = request.form['name']
    new_guest = Guest(name, 0)
    guest_repository.save(new_guest)
    return redirect('/guests')

# SHOW
@guests_blueprint.route('/guests/<id>')
def show_guest(id):
    guest = guest_repository.select(id)
    return render_template('guests/show.html', guest=guest)

# EDIT
@guests_blueprint.route('/guests/<id>/edit')
def edit_guest(id):
    guest = guest_repository.select(id)
    return render_template('guests/edit.html', guest=guest)

# UPDATE
@guests_blueprint.route('/guests/<id>', methods=['POST'])
def update_guest(id):
    name = request.form['name']
    updated_guest = Guest(name, id)
    guest_repository.update(updated_guest)
    return redirect('/guests')

# DELETE
@guests_blueprint.route('/guests/<id>/delete', methods=['POST'])
def delete_guest(id):
    guest_repository.delete(id)
    return redirect('/guests')