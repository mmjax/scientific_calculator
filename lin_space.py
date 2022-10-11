import math


def nonlinear_check(stroka):
    if (stroka.count('=')) == 0:
        return "Это не уравнение"
    else:
        check = False
        if (stroka.count("^") != 0) or (stroka.count("tg") != 0) or \
                (stroka.count("ctg") != 0) or (stroka.count("log") != 0) or \
                (stroka.count("sin") != 0) or (stroka.count("cos") != 0) or \
                (stroka.count("ln") != 0) or (stroka.count("arcsin") != 0) or \
                (stroka.count("arcos") != 0) or (stroka.count("arctg") != 0) or \
                (stroka.count("arcctg") != 0) or (stroka.count("sh") != 0) or \
                (stroka.count("ch") != 0) or (stroka.count("th") != 0):
            s = "Уравнение " + stroka + " нелинейное"
            return s
        else:
            if stroka.count('*') != 0:
                massive = stroka.split('*')
                for i in range(len(massive) - 1):
                    if not (massive[i].isnumeric()) and \
                            not (massive[i + 1].isnumeric()):
                        check = True
                if check:
                    s = "Уравнение " + stroka + " нелинейное"
                    return s
                else:
                    s = "Уравнение " + stroka + " не нелинейное"
                    return s
            else:
                s = "Уравнение " + stroka + " не нелинейное"
                return s


def space_sum_calculator(type_of_figure, type_of_size, a, b, c, h1, h2, d1, d2, sin, r):
    if (a >= 0) and (b >= 0) and (c >= 0) and (h1 >= 0) and (h2 >= 0) and (d2 >= 0) and (d1 >= 0) and (sin >= 0) and (
            r >= 0):
        s = size_calculator(type_of_size, a, b, c, h2, d1, d2, sin, r)
        if s != "Ошибка!":
            match type_of_figure:
                case "Призма":
                    v = s * h1
                    stroka = "Объём призмы равен " + str(v)
                    return stroka
                case "Пирамида":
                    v = s * h1 / 3
                    stroka = "Объём пирамиды равен " + str(v)
                    return stroka
                case "Цилиндр":
                    v = math.pi*r*r*h1
                    stroka = "Объём цилиндра равен" + str(v)
                    return stroka
                case "Конус":
                    v = s * h1/3
                    stroka = "Объём конуса равен" + str(v)
                    return stroka
                case "Шар":
                    v = r*r*r*4*math.pi/3
                    stroka = "Объём шара равен" + str(v)
                    return stroka
        return "Ошибка!"


def size_calculator(type_of_size, a, b, c, h2, d1, d2, sin, r):
    match type_of_size:
        case "Квадрат":
            if a != 0:
                s = a * a
                return s
            return "Ошибка!"
        case "Прямоугольник":
            if (a != 0) and (b != 0):
                s = a * b
                return s
            return "Ошибка!"
        case "Параллелограмм":
            if a != 0:
                if h2 != 0:
                    s = a * h2
                    return s
                else:
                    if sin != 0:
                        s = a * b * sin
                        return s
            return "Ошибка!"
        case "Ромб":
            if a != 0:
                if h2 != 0:
                    s = a * h2
                    return s
                if sin != 0:
                    s = a * a * sin
                    return s
                if d1 != 0 and d2 != 0:
                    s = d1 * d2 / 2
                    return s
            return "Ошибка!"
        case "Трапеция":
            if (a != 0) and (b != 0) and (h2 != 0):
                s = (a + b) * h2 / 2
                return s
            return "Ошибка!"
        case "Круг":
            if r != 0:
                s = math.pi * r * r
                return s
            return "Ошибка!"
        case "Треугольник":
            if a != 0:
                if h2 != 0:
                    s = a * h2 / 2
                    return s
                if b != 0:
                    if sin != 0:
                        s = a * b * sin / 2
                        return s
                    if c != 0 and r != 0:
                        s = (a + b + c) / 2 * r
            return "Ошибка!"
    return "Ошибка!"
