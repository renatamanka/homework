"""
С помощью обработки ошибок разделить все элементы этого списка на 3.
При возникновении ошибки вывести надпись "Невозможно разделить"
"""


lst = ["Максим",12,14,"Олег","100"]
for i in lst:
    try:
        print(i/3)
    except:
        print('Невозможно разделить')
