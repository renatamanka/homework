a = list(map(int, input('Введите список цифр: ').split()))
fun = 1
for num in a:
    if num - fun == 1:
        fun = num
        s = 'Да'
    elif len(a) <= 1:
        s = 'нет'
    else:
        s = 'нет'
print(s)
