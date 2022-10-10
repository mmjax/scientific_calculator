import unittest
from numbers import Integral

import pytest
from sympy import integrate
from sympy.abc import x

from main import integr, kvad


def test_integr():
    expr = x**2
    assert integrate(expr, x) == x**3/3

def test_kvad():
    assert kvad(3, -2, 2) == 'Нет корней'
