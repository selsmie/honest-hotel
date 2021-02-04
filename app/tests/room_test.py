import unittest
from models.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room(1)
        self.room_2 = Room(2)

    def test_room_has_number_1(self):
        self.assertEqual(1, self.room_1.room_number)

    def test_room_has_number_2(self):
        self.assertEqual(2, self.room_2.room_number)