a, b = int(input()), int(input())
while a != b :
    if a > b : a = a - b    # a -= b
    if b > a : b = b - a    # b -= a
print(a)
