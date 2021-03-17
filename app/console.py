import pdb

from models.guest import Guest
from models.room import Room
from models.reservation import Reservation

import repositories.guest_repository as guest_repository
import repositories.room_repository as room_repository
import repositories.reservation_repository as reservation_repository

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


pdb.set_trace()