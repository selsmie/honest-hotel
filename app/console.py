import pdb

from models.guest import Guest
import repositories.guest_repository as guest_repository

from models.resevation import Reservation
from models.room import Room

guest_1 = Guest("Rick", "Sanchez")
guest_repository.save(guest_1)
guest_2 = Guest("Morty", "Smith")
guest_repository.save(guest_2)

pdb.set_trace()