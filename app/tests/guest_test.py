import unittest

from models.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Simon Elsmie", 0)
        self.guest_2 = Guest("Rick Sanchez", 0)

    def test_guest_1_name(self):
        self.assertEqual("Simon Elsmie", self.guest_1.name)

    def test_guest_2_name(self):
        self.assertEqual("Rick Sanchez", self.guest_2.name)

    def test_stay_count_increase(self):
        self.guest_1.increase_stay_count()
        self.assertEqual(1, self.guest_1.stays)