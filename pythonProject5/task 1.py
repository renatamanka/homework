lst = []
i = input('Напишите игру: ')
while i != '0':
    if i not in lst:
        lst.append(i)
    else:
        print('Такая игра уже есть')
    i = input('Напишите игру: ')
print('завершено')
lst.sort()
print(lst)

