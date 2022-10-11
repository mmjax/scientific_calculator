import unittest
from main import nonlinear_check, space_sum_calculator, size_calculator


class MyTestCase(unittest.TestCase):

    def test_result(self):
        self.assertEqual(nonlinear_check("x*y=0"), "Уравнение x*y=0 нелинейное")
        self.assertEqual(nonlinear_check("x+y=0"), "Уравнение x+y=0 не нелинейное")
        self.assertEqual(space_sum_calculator("Призма", "Квадрат", 4, 0, 0, 5, 0, 0, 0, 0, 0), "Объём призмы равен 80")
