# Задание 3:
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_number = int(input("Введите целое число от 1 до 9 >>> "))
double_user_number = user_number * 10 + user_number
triple_double_user_number = double_user_number * 10 + user_number
sum = user_number + double_user_number + triple_double_user_number

print(f"Сумма чисел в формате n + nn + nnn >>> {sum}")
