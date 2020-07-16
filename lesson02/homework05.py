# Задача-5: Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
user_number = int(input("Введите новый элемент рейтинга >>> "))
while True:
    for el in range(len(my_list)):
        if my_list[el] == user_number:
            my_list.insert(el + 1, user_number)
            break
        elif my_list[0] < user_number:
            my_list.insert(0, user_number)
        elif my_list[-1] > user_number:
            my_list.append(user_number)
        elif my_list[el] > user_number > my_list[el + 1]:
            my_list.insert(el + 1, user_number)
    print(f"текущий список - {my_list}")
    user_number = int(input("Введите новый элемент рейтинга >>> "))
