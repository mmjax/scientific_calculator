from matrix import input_matrix
from simple import simple_calculator
from integer import integr, kvad


while True:
    print("выберите что вы хотите сделать:\n1.Матричный калькулятор\n2.Обычный калькулятор\n3.Интеграл\n4.Квадратное кравнение\nq чтобы выйти")
    choice = input()
    if choice == "1":
        input_matrix()
    elif choice == "2":
        simple_calculator()
    elif choice == "3":
        print(integr())
    elif choice == "4":
        print(kvad())
    if choice == "q":
        break
    else:
        print("Такой операции нет, попробуйте ещё раз")

