from flask import Flask, redirect, render_template, request, Blueprint

from models.guest import Guest
import repositories.guest_repository as guest_repository

guests_blueprint = Blueprint("guests", __name__)

@guests_blueprint.route('/guests')
def guests():
    guests = guest_repository.select_all()
    print(guests)
    return render_template('guests/guest.html', guests=guests)

@guests_blueprint.route('/guests/new')
def new_guest():
    return render_template('guests/new.html')

@guests_blueprint.route('/guests', methods=['POST'])
def create_guest():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    new_guest = Guest(first_name, last_name)
    guest_repository.save(new_guest)
    return redirect('/guests')

@guests_blueprint.route('/guests/<id>/edit')
def edit_human(id):
    guest = guest_repository.select(id)
    return render_template('guests/edit.html', guest=guest)

@guests_blueprint.route('/guests/<id>', methods=['POST'])
def update_guest(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    guest = Guest(first_name, last_name, id)
    guest_repository.update(guest)
    return redirect('/guests')

@guests_blueprint.route('/guests/<id>/delete', methods=['POST'])
def delete_guest(id):
    guest_repository.delete(id)
    return redirect('/guests')