import math

from sympy import *

def integr ():
    while True:
        x, y = symbols('x y')
        print('Введите то, что хотите интегрировать, или если хотите выйти нажмите q')
        expr = input()
        if expr == 'q':
            break
        return (integrate(expr, x))


def kvad ():
    while True:
        a = input("введите a(либо если хотеите прекратить нажмите q):")
        if a == 'q':
            break
        b = int(input("введите b:"))
        c = int(input("введите c:"))
        a = int(a)
        dis_form = b * b - 4 * a * c
        sqrt_val = math.sqrt(abs(dis_form))

        if dis_form > 0:
            return ((-b + sqrt_val) / (2 * a))

        elif dis_form == 0:
            return (-b / (2 * a))

        else:
            return ('Нет корней')
