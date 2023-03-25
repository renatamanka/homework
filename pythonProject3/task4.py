categoria = input('Введите категорию: ')
if categoria == 'Продукты':
    money = int(input('Введите цену: '))
    if money < 100:
        print('Попробуйте нашу выпечку!')
    elif 100 <= money < 500:
        print('Как насчет орехов в шоколаде?')
    elif money >= 500:
        print('Попробуйте экзотические фрукты!')
else:
    print('Заглянитев товары для дома')
