import unittest
from square import circle, rectangle
from math import pi

class square_test(unittest.TestCase):
    def test_circle(self):
        self.assertEqual(circle(3),pi*3**2)
        self.assertEqual(circle(1),pi)
        self.assertEqual(circle(6),6)
        self.assertEqual(circle(4.5),pi*4.5**2)

    def test_rectangle(self):
        self.assertEqual(rectangle(10,10), 10*10)
        self.assertEqual(rectangle(15,2), 15*2)
        self.assertEqual(rectangle(5,2), 5*2)
        self.assertEqual(rectangle(3,6), 3*6)
