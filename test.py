import unittest
from controller.db import get_flights, get_plane_list


class TestDBRequests(unittest.TestCase):

    def test_get_plane_list(self):
        plane = get_plane_list()
        self.assertEqual(plane[0], "UA-24")

    def test_get_flights_by_plane_number(self):
        flight = get_flights("КА-124", "")[0]
        self.assertEqual(flight[1], "КА-124")

    def test_get_flights_by_hours(self):
        flights = get_flights('', 15)
        for flight in flights:
            with self.subTest(flight=flight):
                is_bigger = flight[2] >= 15
                self.assertEqual(is_bigger, True)

    def test_get_flights_without_parameters(self):
        flights = get_flights('', '')
        is_empty = len(flights) <= 0

        self.assertEqual(is_empty, False)
