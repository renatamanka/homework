a = list(map(int, input('Введите оценки: ').split()))
sun = 0
nun = 0
for i in a:
    nun += 1
    if i == 5:
        sun += 1
print((sun / nun) * 100)

