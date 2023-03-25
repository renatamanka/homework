login = input('Введите логин: ')
sim = '=?*^$№@_ '
for i in login:
    if i in sim:
        print(i)
