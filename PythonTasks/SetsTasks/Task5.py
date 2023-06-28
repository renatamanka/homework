"""
Каждый из N школьников некоторой школы знает M языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
Входные данные:
Сначала запрашивается количество учеников(например 6).
Дальше запрашивается количество учеников знающих определенный набор языков и языки которые они знают
Например:
3
Russian
English
Japanese
2
Russian
English
1
English
Вывод должен быть:
3 - [Russian, English,Japenese]
1 - [English]
"""
sum1 = 0
sum2 = 0
sum3 = 0

all = int(input('Сколько всего учеников? '))
group_1 = int(input('Количество учеников, знающих определенный набор языков: '))
lang_1 = (input('Какие языки они знают? ')).split()
group_2 = int(input('Количество учеников, знающих определенный набор языков: '))
lang_2 = (input('Какие языки они знают? ')).split()
group_3 = int(input('Количество учеников, знающих определенный набор языков: '))
lang_3 = (input('Какие языки они знают? ')).split()
for a in lang_1:
    for b in lang_2:
        for c in lang_3:
            if a == b == c:
                print('этот язык знают все в группе: ', a)
if len(lang_1) > len(lang_2) and len(lang_1) > len(lang_3):
    print(group_1,'-', lang_1)
elif len(lang_2) > len(lang_1) and len(lang_2) > len(lang_3):
    print(group_2,'-', lang_2)
elif len(lang_3) > len(lang_2) and len(lang_3) > len(lang_1):
    print(group_3,'-', lang_3)
