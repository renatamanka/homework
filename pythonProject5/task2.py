marks = [1, 2, 3, 4, 5, 3, 4, 5, 2, 1]
sun = 0
nun = 0
for i in marks:
    nun += 1
    if i > 2:
        sun += 1
print(marks)
print(nun)
print((sun/ nun) * 100)

