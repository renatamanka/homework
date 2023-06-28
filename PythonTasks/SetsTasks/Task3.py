"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите сколько семей живёт в доме N.
"""
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
newspaper1 = set(newspaper)
magazine1 = set(magazine)
both1 = set(both)

all = (newspaper1 | magazine1) - both1
sum = 0
for i in all:
    sum +=1
print(sum)