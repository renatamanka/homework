a, b, c = input('Введите суммы трех товаров: ').split(',')
a, b, c = [int(a), int(b), int(c)]
if a < b < c:
    print('Акция! К оплате: ', (a + b + c) // 2)
elif c < b < a:
    print('Акция! К оплате: ', (a + b + c) // 3)
else:
    print('К оплате: ', (a + b + c))
