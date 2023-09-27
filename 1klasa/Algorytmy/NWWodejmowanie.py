a, b = int(input()), int(input())
iloczyn = a*b
while a != b:
  if a > b: a -= b
  if b > a: b -= a
print(iloczyn // a)