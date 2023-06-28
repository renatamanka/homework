"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, то должна выполняться конкатенация, то есть соединение, строк.
В остальных случаях введенные числа суммируются.
"""
first = input('Введите значение: ')
second = input('Введите значение: ')
try:
    first = int(first)
    second = int(second)
except:
    first = str(first)
    second = str(second)
finally:
    print(first + second)

