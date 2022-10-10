from unittest import TestCase, main
from simple import add, muliply, div, subtract

class simple_test(TestCase):
    def test_correct_result_of_add(self):
        self.assertEqual(add(2, 3), '2.00 + 3.00 = 5.00')
    
    def test_correct_result_of_subtract(self):
        self.assertEqual(subtract(5, 3), '5.00 - 3.00 = 2.00')

    def test_correct_result_of_muliply(self):
        self.assertEqual(muliply(5, 3), '5.00 * 3.00 = 15.00')

    def test_correct_result_of_div(self):
        self.assertEqual(div(6, 3), '6.00 / 3.00 = 2.00')
    
    def test_bad_result_of_div(self):
        self.assertEqual(div(6, 0), 'Деление на ноль!')
    
    def test_correct_result_of_subtract2(self):
        self.assertEqual(subtract(1, 3), '1.00 - 3.00 = -2.00')
    
    def test_correct_result_of_div2(self):
        self.assertEqual(div(6, 4), '6.00 / 4.00 = 1.50')

    def test_correct_result_of_div_by_zero(self):
        self.assertEqual(div(0, 4), '0.00 / 4.00 = 0.00')
