# Задание 2:
# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_sec = int(input("Введите время в секундах >>> "))
hours = time_in_sec // 3600
remainder = time_in_sec % 3600
minutes = remainder // 60
sec = remainder % 60
print(f"Введенные секунды в формате  в формате чч:мм:сс >> {hours}:{minutes}:{sec} ")