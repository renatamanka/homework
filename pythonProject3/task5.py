num = int(input('Введите число: '))
sum = 0
if num % 10 !=0:
    if (num % 10) % 2 == 0:
       # a = [int(b) for b in str(num)]
        for n in range( len(str(num))):
            sum += n
            if sum % 3 ==0:
                print('кратно 6')
    else:
        print('не кратно 6')
elif num == 6:
    print('кратно 6')
else:
    print('не делится на 6')
