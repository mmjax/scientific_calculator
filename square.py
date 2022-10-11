import math
def square():
    while True:
        print("Выберите площадь какой фигуры вы хотите найти: \n"
            "Площадь круга: Круг\n"
            "Площадь Прямоугольника: Прямоугольник\n"
        )
        action = input("Действие: ")
        if action == "q":
            print("Выход из программы")
            break
        if action == ("Круг"):
            r = float(input("Радиус = "))
            print(circle(r))
        if action == ("Прямоугольник"):
            x = float(input("Сторона x = "))
            y = float(input("Сторона y = "))
            print(rectangle(x, y))

def circle(r):
    if r > 0:
        print("Площадь круга равна: ") 
        return  math.pi * (r ** 2)
    else:
        return print('Радиус не может быть нулем или отрицательным числом!')
    

def rectangle(x,y):
    if x or y > 0:
        print("Площадь прямоугольника равна: ")
        return (x * y)
    else:
        return print('Сторона не может быть отрицательной или равна нулю')
