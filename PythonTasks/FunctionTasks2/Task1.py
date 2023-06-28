"""
Создайте функцию которая принимает на вход 3 именованных параметра, выведите на печать значения этих параметров,
но только в том случае если они не равны None.
"""


def trying(name, age, high):
    if name is not None and age is not None and high is not None:
        print(name,age,high)
    else:
        print('Ошибка')
print(trying('renata',None,140))