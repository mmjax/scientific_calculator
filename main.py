from matrix import input_matrix
from simple import simple_calculator


while True:
    print("выберите что вы хотите сделать:\n1.Матричный калькулятор\n2.Обычный калькулятор\nq чтобы выйти")
    choice = input()
    if choice == "1":
        input_matrix()
    if choice == "2":
        simple_calculator()
    if choice == "q":
        break
    else:
        print("Такой операции нет, попробуйте ещё раз")

