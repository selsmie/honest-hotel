import pdb

from models.guest import Guest
from models.room import Room
from models.reservation import Reservation

import repositories.guest_repository as guest_repository
import repositories.room_repository as room_repository
import repositories.reservation_repository as reservation_repository

guest_1 = Guest("Rick Sanchez")
guest_repository.save(guest_1)
guest_2 = Guest("Morty Smith")
guest_repository.save(guest_2)
guest_3 = Guest("Summer Smith")
guest_repository.save(guest_3)
guest_4 = Guest("Beth Smith")
guest_repository.save(guest_4)
guest_5 = Guest("Jerry Smith")
guest_repository.save(guest_5)
guest_6 = Guest("Simon Elsmie")
guest_repository.save(guest_6)

room_0 = Room(0, 0)
room_repository.save(room_0)

room_1 = Room(1)
room_repository.save(room_1)
room_2 = Room(2)
room_repository.save(room_2)
room_3 = Room(3)
room_repository.save(room_3)
room_4 = Room(4)
room_repository.save(room_4)
room_5 = Room(5)
room_repository.save(room_5)


arr_date_1 = '2021-02-11'
dep_date_1 = '2021-02-13'
arr_date_2 = '2021-02-12'
dep_date_2 = '2021-02-14'
arr_date_3 = '2021-03-11'
dep_date_3 = '2021-03-13'

res_1 = Reservation(guest_1, room_0, arr_date_1, dep_date_2, "Arrival")
reservation_repository.save(res_1)
res_2 = Reservation(guest_2, room_0, arr_date_1, dep_date_2, "Arrival")
reservation_repository.save(res_2)
res_3 = Reservation(guest_3, room_0, arr_date_1, dep_date_1, "Arrival")
reservation_repository.save(res_3)
res_4 = Reservation(guest_4, room_0, arr_date_1, dep_date_1, "Arrival")
reservation_repository.save(res_4)
res_5 = Reservation(guest_5, room_0, arr_date_3, dep_date_3, "Arrival")
reservation_repository.save(res_5)
res_6 = Reservation(guest_6, room_5, '2021-02-09', '2021-02-11', "Arrival")
reservation_repository.save(res_6)

pdb.set_trace()