import unittest
import datetime

from models.reservation import Reservation
from models.guest import Guest
from models.room import Room

class TestReservation(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Simon Elsmie")
        self.guest_2 = Guest("Rick Sanchez")
        self.room_1 = Room(1)
        self.room_2 = Room(2)
        self.date_1 = '2021-04-06'
        self.date_2 = '2021-04-07'
        self.reservation_1 = Reservation(self.guest_1, self.room_2, self.date_1, self.date_2, "Arrival")
        self.reservation_2 = Reservation(self.guest_2, self.room_1, self.date_1, self.date_2, "Arrival")

    # @unittest.skip
    def test_reservation_1_has_guest(self):
        name = self.reservation_1.guest.name
        self.assertEqual("Simon Elsmie", name)

    # @unittest.skip
    def test_reservation_2_has_guest(self):
        name = self.reservation_2.guest.name
        self.assertEqual("Rick Sanchez", name)

    # @unittest.skip
    def test_reservation_2_has_number(self):
        number = self.reservation_2.room.room_number
        self.assertEqual(1, number)

    # @unittest.skip
    def test_reservation_1_has_number(self):
        number = self.reservation_1.room.room_number
        self.assertEqual(2, number)

    def test_res_1_has_arr_date(self):
        print(self.reservation_1.guest.name)
        print(self.reservation_1.room.room_number)
        print(self.reservation_1.arrival_date)
        print(self.reservation_1.departure_date)
        print(self.reservation_1.status)

        self.assertEqual('2021-04-06', self.reservation_1.arrival_date)

    