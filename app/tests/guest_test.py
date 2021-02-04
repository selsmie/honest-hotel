import unittest
from models.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Simon", "Elsmie")
        self.guest_2 = Guest("Rick", "Sanchez")

    def test_guest_first_name(self):
        self.assertEqual("Simon", self.guest_1.first_name)

    def test_guest_last_name(self):
        self.assertEqual("Sanchez", self.guest_2.last_name)