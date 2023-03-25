start = input('Чтобы начать игру введите "game". Чтобы закончить игру введите "off": ')
while start == 'game':
    for i in range(0, 3):
       num = int(input('Угадай число! '))
       if num == 5:
           print('Ты угадал!')
           break
       else:
           print('Не угадал')
    print('Игра окончена')
    start = input('Чтобы начать игру введите "game". Чтобы закончить игру введите "off": ')
print('Игра окончена')




