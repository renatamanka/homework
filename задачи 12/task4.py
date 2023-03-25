max = 0
min = 0
sum = 0
ferst_num = int(input('Введите первое число: '))
sec_num = int(input('Введите второе число: '))
third_num = int(input('Введите третье число: '))
sum = ferst_num + sec_num + third_num
if ferst_num > sec_num and ferst_num > third_num:
    max = ferst_num
    if sec_num > third_num:
        min = third_num
    else:
        min = sec_num
elif sec_num > ferst_num and sec_num > third_num:
    max = sec_num
    if ferst_num > third_num:
        min = third_num
    else:
        min = ferst_num
else:
    max = third_num
    if ferst_num > sec_num:
        min = sec_num
    else:
        min = ferst_num
print(sum, max, min)