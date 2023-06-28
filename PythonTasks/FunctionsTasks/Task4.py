"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""


def imt(weight, height):
    index = weight / (height * height)
    return index


def results(index):
    if index < 18.5:
        print('Недостаточный вес')
    elif index >= 18.5 and index < 25:
        print('ИМТ в норме')
    else:
        print('Избыточный вес')


start = int(input('Чтобы рассчитать индекс массы тела нажмите "1", чтобы завершить программу нажмите "0" '))
while start != 0:
    weight = int(input('Введите свой вес в кг: '))
    height = float(input('Введите свой рост в метрах: '))
    imt(weight, height)
    results(imt(weight, height))
    start = int(input('Чтобы рассчитать индекс массы тела нажмите "1", чтобы завершить программу нажмите "0" '))

