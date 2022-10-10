def simple_calculator():
    while True:
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")
        action = input("Действие: ")
        if action == "q":
            print("Выход из программы")
            break
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                print(add(x, y))
            elif action == '-':
                print(subtract(x, y))
            elif action == '*':
                print(muliply(x, y))
            elif action == '/':
                print(div(x, y))

def add(x, y):
    return ('%.2f + %.2f = %.2f' % (x, y, x+y))

def subtract(x, y):
    return ('%.2f - %.2f = %.2f' % (x, y, x-y))

def muliply(x, y):
    return ('%.2f * %.2f = %.2f' % (x, y, x*y))

def div(x, y):
    if y != 0:
        return ('%.2f / %.2f = %.2f' % (x, y, x/y))
    else:
        return("Деление на ноль!")