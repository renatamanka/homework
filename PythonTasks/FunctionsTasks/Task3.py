"""
Напишите программу определяющую допуск ученика к зачету.
Программа должна запрашивать число учеников, затем у каждого ученика запрашивать балл за финальный тест
и в ответ печатать, допущен ли он (True или False) к зачету (необходимо набрать больше 50 баллов).

Ученикам без допуска должно печататься "Вы отчислены".

Выдачу допуска реализуй как функцию.
"""
def allowance(scores):
    if scores > 50:
        print('Вы допущены к зачету. Поздравляем! ')
    else:
        print('Вы отчислены.')
students = int(input('Количество учеников: '))
for i in range(students):
    scores = int(input('Введите балл за финальный тест: '))
    allowance(scores)