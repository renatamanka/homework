a = float(input())
h = float(input())
rashod = int(input())
banka = int(input())11
zapas = int(input())
s = a * h
l = (s / rashod)
m = 20 / 100 * l
l += m

print(round(s, 2))
print(round(l, 2))
print( l // banka + 1)


