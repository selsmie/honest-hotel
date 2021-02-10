from flask import Flask, redirect, render_template, request, Blueprint

from models.guest import Guest
import repositories.guest_repository as guest_repository
import repositories.reservation_repository as reservation_repository

guests_blueprint = Blueprint("guests", __name__)

# INDEX
@guests_blueprint.route('/guests')
def guests():
    guests = guest_repository.select_all()
    reservation_repository.arrival_staus()
    return render_template('guests/guest.html', guests=guests)

# NEW
@guests_blueprint.route('/guests/new')
def new_guest():
    return render_template('guests/new.html')

# CREATE
@guests_blueprint.route('/guests', methods=['POST'])
def create_guest():
    name = request.form['name']
    new_guest = Guest(name)
    guest_repository.save(new_guest)
    return redirect('/guests')

# EDIT
@guests_blueprint.route('/guests/<id>/edit')
def edit_guest(id):
    guest = guest_repository.select(id)
    return render_template('guests/edit.html', guest=guest)

# UPDATE
@guests_blueprint.route('/guests/<id>', methods=['POST'])
def update_guest(id):
    name = request.form['name']
    stays = request.form['stays']
    preferences = request.form['preferences']
    updated_guest = Guest(name, stays, preferences, id)
    guest_repository.update(updated_guest)
    return redirect('/guests')

# DELETE
@guests_blueprint.route('/guests/<id>/delete')
def delete_guest(id):
    guest = guest_repository.select(id)
    return render_template('guests/delete.html', guest=guest)

@guests_blueprint.route('/guests/<id>/delete', methods=['POST'])
def delete_confirm(id):
    guest_repository.delete(id)
    return redirect('/guests')

# Preferences
@guests_blueprint.route('/guests/<id>/preferences')
def guest_preferences(id):
    guest = guest_repository.select(id)
    return render_template('guests/preference.html', guest=guest)

# Search
@guests_blueprint.route('/guests/search', methods=['POST'])
def search_name():
    search_name = request.form['search']
    guest = guest_repository.search(search_name)
    return render_template('guests/preference.html', guest=guest)