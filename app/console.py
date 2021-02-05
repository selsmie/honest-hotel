import pdb

from models.guest import Guest
from models.room import Room
from models.reservation import Reservation

import repositories.guest_repository as guest_repository
import repositories.room_repository as room_repository
import repositories.reservation_repository as reservation_repository

guest_1 = Guest("Rick", "Sanchez")
guest_repository.save(guest_1)
guest_2 = Guest("Morty", "Smith")
guest_repository.save(guest_2)
guest_3 = Guest("Summer", "Smith")
guest_repository.save(guest_3)
guest_4 = Guest("Beth", "Smith")
guest_repository.save(guest_4)
guest_5 = Guest("Jerry", "Smith")
guest_repository.save(guest_5)

room_1 = Room(1)
room_repository.save(room_1)
room_2 = Room(2)
room_repository.save(room_2)
room_3 = Room(3)
room_repository.save(room_3)

reservation_1 = Reservation(guest_1, room_1)
reservation_repository.save(reservation_1)
reservation_2 = Reservation(guest_2, room_3)
reservation_repository.save(reservation_2)


pdb.set_trace()