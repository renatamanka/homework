"""
В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
Предлагать ввод хода (например, E2–E4) и считать потраченное время.
После получения хода печатать оставшееся время в минутах.
Если 30 минут закончились или игрок вводит «off» — завершать работу.
Оформить в виде функции.
"""
from time import time
from random import randint, choice

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def chess(letters):
    gambit = randint(1,8)
    #letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    letter = choice(letters)
    print('Сходите так: ', letter, gambit, '-', letter, gambit+2)
play = input('Ваш ход? (off - завершить)')
while play != 'off':
    start = time()
    chess(letters)
    end = time()
    print('Ход длился: ', (end - start), 'Осталось: ', (1800 - end + start))
    play = input('Ваш ход? (off - завершить)')
    if (end - start) > 1800:
        break
        print('Ход завершен')
else:
    print('Ход завершен')


