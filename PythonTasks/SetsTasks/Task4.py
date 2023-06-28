"""
Вася давно мечтает выиграть олимпиаду по информатике.
У него всего три слабых места: циклы, массивы и строки.
Перед сегодняшним турниром Вася провёл интенсивную подготовку, в ходе которой он решил A задач на циклы,
B задач на массивы и C задач на строки.
Впоследствии выяснилось, что из решённых задач D были и на циклы, и на массивы, E – на циклы и на строки,
F – на строки и на массивы. И даже было G задач, которые включали и циклы, и строки, и массивы.
Помогите Васе вычислить, сколько всего различных задач он решил.
Введите результат для всех 3 входных данных
"""
first = "0 0 0 0 0 0 0" #Вывод должен быть 0
second = "1 1 1 0 0 0 0" # Вывод должен быть 3
third = "1 1 1 1 1 1 1" # Вывод должен быть 1
#a+b+c-d-f-e+g
f = first.split()
s = second.split()
t = third.split()
f = list(map(int, f))
s = list(map(int, s))
t = list(map(int, t))
print((f[0] + f[1] + f[2]) - (f[3] -f[4] - f[5]) + f[6])
print((t[0] + t[1] + t[2]) - (t[3] + t[4] + t[5]) + t[6])
print((s[0] + s[1] + s[2]) - (s[3] + s[4] + s[5]) + s[6])



