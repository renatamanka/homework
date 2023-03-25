money = int(input('Введите сумму: '))
hours = int(input('Который сейчас час? ')[0:2])
if 10 <= hours <= 12:
    print('Оплатите: ' , money // 2)
elif 20 <= hours <= 22:
    print('Оплатите: ' , money // 4)
elif 8 < hours < 10 or 12 < hours < 20:
    print('Оплатите: ' , money)
else:
    print('А мы не работаем(((')


