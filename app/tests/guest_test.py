import unittest
from models.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Simon", "Elsmie")
        self.guest_2 = Guest("Rick", "Sanchez")

    def test_guest_first_name(self):
        self.assertEqual("Simon Elsmie", self.guest_1.name)

    def test_guest_last_name(self):
        self.assertEqual("Rick Sanchez", self.guest_2.name)