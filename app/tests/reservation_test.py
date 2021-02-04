import unittest

from models.resevation import Reservation
from models.guest import Guest
from models.room import Room

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Simon", "Elsmie")
        self.guest_2 = Guest("Rick", "Sanchez")
        self.room_1 = Room(1)
        self.room_2 = Room(2)
        self.reservation_1 = Reservation(self.guest_1, self.room_2)
        self.reservation_2 = Reservation(self.guest_2, self.room_1)

    def test_reservation_1_has_guest(self):
        first_name = self.reservation_1.guest.first_name
        self.assertEqual("Simon", first_name)

    def test_reservation_2_has_guest(self):
        first_name = self.reservation_2.guest.first_name
        self.assertEqual("Rick", first_name)

    def test_reservation_2_has_number(self):
        number = self.reservation_2.room.room_number
        self.assertEqual(1, number)

    def test_reservation_1_has_number(self):
        number = self.reservation_1.room.room_number
        self.assertEqual(2, number)