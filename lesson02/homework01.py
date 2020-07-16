# Задание 1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

value_int = 20
value_str = "Hello world"
value_list = ['1', '2']
value_tuple = ('10', '3')
value_dict = {'Name': 'John', 'city': 'Moscow'}

new_list = [value_int, value_str, value_list, value_tuple, value_dict]
for value in new_list:
    print(f'{value} is {type(value)}')