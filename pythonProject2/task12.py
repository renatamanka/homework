str = input('Ввод: ')
num = str.replace('<span>', '').replace('&nbsp;', '').replace('P</span>', '')
num_2 = int(num)
print(num_2 + 1)
