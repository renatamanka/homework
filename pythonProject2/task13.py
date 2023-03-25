str = input('Ввод: ')
strs = str.split(' ')
for a in strs:
    if '@' in a:
        print(a)
