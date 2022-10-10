from unittest import TestCase, main
from matrix import add_matrix, subtract_matrix
import numpy as np
import pytest


class matrix_test(TestCase):
    def test_correct_result_of_add(self):
        m = np.array([[1, 2, 3], [5, 6, 7]])
        m2 = np.array([[3, 2, 5], [9, 0, 4]])
        r = np.array([[4, 4, 8], [14, 6, 11]])
        self.assertEqual(add_matrix(m.all(), m2.all()), r.all())
    
    def test_error_result_of_diff(self):
        with pytest.raises(ValueError):
            matrix1 = [[1, 2, 3], [5, 6, 7], [5, 3, 6]]
            matrix2 = [[3, 2, 5], [9, 0, 4]]
            assert add_matrix(matrix1, matrix2) == ValueError
    

if __name__ == '__main__':
    main()