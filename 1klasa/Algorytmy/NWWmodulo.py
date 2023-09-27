a, b = int(input()), int(input())
iloczyn = a * b
while b > 0:
    a, b = b,a %b
print(iloczyn // a)