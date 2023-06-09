"""
Представьте, что сумма за пользование услугами такси складывается из
базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
Напишите функцию, принимающую в качестве единственного параметра
расстояние поездки в километрах и возвращающую итоговую сумму опла-
ты такси.
"""
km = int(input('Введите расстояние в км: '))
metres = km * 1000


def cost(metres):
    if metres < 140:
        return 4.25
    else:
        return 0.25 + cost(metres - 140)

print(cost(metres))